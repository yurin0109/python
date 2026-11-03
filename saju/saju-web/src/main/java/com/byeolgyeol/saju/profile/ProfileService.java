package com.byeolgyeol.saju.profile;

import com.byeolgyeol.saju.calc.Pillar;
import com.byeolgyeol.saju.calc.SajuCalculator;
import com.byeolgyeol.saju.calc.SajuChart;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.List;
import java.util.NoSuchElementException;

@Service
@Transactional(readOnly = true)
public class ProfileService {

    private static final ZoneId KOREA = ZoneId.of("Asia/Seoul");

    private final ProfileRepository repository;
    private final ReflectionRepository reflectionRepository;
    private final SajuCalculator calculator = new SajuCalculator();

    public ProfileService(ProfileRepository repository, ReflectionRepository reflectionRepository) {
        this.repository = repository;
        this.reflectionRepository = reflectionRepository;
    }

    public List<ProfileResponse> findAll(String clientId) {
        return repository.findByClientIdOrderByCreatedAtDesc(clientId).stream()
                .map(this::toResponse)
                .toList();
    }

    public ProfileResponse findOne(String clientId, Long id) {
        return toResponse(get(clientId, id));
    }

    @Transactional
    public ProfileResponse create(String clientId, ProfileRequest req) {
        Profile saved = repository.save(new Profile(clientId, req.name().trim(), req.birthDate(),
                req.birthTime(), req.gender(), blankToNull(req.birthPlace())));
        return toResponse(saved);
    }

    @Transactional
    public ProfileResponse update(String clientId, Long id, ProfileRequest req) {
        Profile p = get(clientId, id);
        p.update(req.name().trim(), req.birthDate(), req.birthTime(), req.gender(),
                blankToNull(req.birthPlace()));
        return toResponse(p);
    }

    @Transactional
    public void delete(String clientId, Long id) {
        Profile p = get(clientId, id);
        // 프로필을 지우면 그 프로필로 쓴 성찰 일기도 함께 지운다
        reflectionRepository.deleteByClientIdAndProfileId(clientId, p.getId());
        repository.delete(p);
    }

    private Profile get(String clientId, Long id) {
        return repository.findByIdAndClientId(id, clientId)
                .orElseThrow(() -> new NoSuchElementException("사주 프로필을 찾을 수 없어요."));
    }

    /** 사주는 DB에 저장하지 않고 조회할 때마다 계산한다 (계산이 가볍고, 로직을 고쳐도 바로 반영됨) */
    private ProfileResponse toResponse(Profile p) {
        SajuChart chart = calculator.calculate(p.getBirthDate(), p.getBirthTime());

        // 올해 = 오늘 날짜 기준 사주상 연도 (입춘 전이면 작년)
        int thisYear = calculator.sajuYear(LocalDate.now(KOREA));
        Pillar yearPillar = calculator.yearPillarOf(thisYear);

        return ProfileResponse.of(p, chart, thisYear, yearPillar);
    }

    private static String blankToNull(String s) {
        return (s == null || s.isBlank()) ? null : s.trim();
    }
}
