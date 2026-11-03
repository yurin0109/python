package com.byeolgyeol.saju.profile;

import com.byeolgyeol.saju.calc.*;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

/**
 * 화면에 내려주는 응답.
 * 프로필 정보 + 사주 원국 + 핵심 성향 + 오행 + 올해 운세를 한 번에 담는다.
 */
public record ProfileResponse(
        Long id,
        String name,
        LocalDate birthDate,
        LocalTime birthTime,
        String gender,
        String birthPlace,
        Saju saju
) {

    public record PillarDto(String label, String korean, String hanja,
                            String stemElement, String branchElement) {
        static PillarDto of(String label, Pillar p) {
            if (p == null) return new PillarDto(label, null, null, null, null);
            return new PillarDto(label, p.korean(), p.hanja(),
                    p.stem().element().name(), p.branch().element().name());
        }
    }

    public record ElementDto(String code, String korean, String hanja, String meaning,
                             String trait, int percent) {}

    public record CoreDto(String dayMaster, String dayMasterHanja, String dayMasterElement,
                          String headline, String description, List<String> keywords) {}

    public record BalanceDto(String strongest, String strongText,
                             String weakest, String weakTip, String reflection) {}

    public record YearDto(int year, String pillar, String pillarHanja, String yearElement,
                          String relation, String relationDesc, String title,
                          String keywords, String caution, String body, String action) {}

    public record Saju(List<PillarDto> pillars, List<ElementDto> elements,
                       CoreDto core, BalanceDto balance, YearDto thisYear) {}

    public static ProfileResponse of(Profile p, SajuChart chart, int currentSajuYear, Pillar yearPillar) {
        // 기둥 (시 · 일 · 월 · 년 순서가 전통 표기)
        List<PillarDto> pillars = List.of(
                PillarDto.of("시주", chart.hour()),
                PillarDto.of("일주", chart.day()),
                PillarDto.of("월주", chart.month()),
                PillarDto.of("년주", chart.year()));

        // 오행
        List<ElementDto> elements = new ArrayList<>();
        for (Element e : Element.values()) {
            elements.add(new ElementDto(e.name(), e.korean(), e.hanja(), e.meaning(),
                    Interpretation.ELEMENT.get(e).trait(), chart.elementPercent().get(e)));
        }

        // 핵심 성향 (일간)
        Stem dm = chart.dayMaster();
        Interpretation.DayMasterText dt = Interpretation.DAY_MASTER.get(dm);
        CoreDto core = new CoreDto(dm.korean(), dm.hanja(), dm.element().name(),
                dt.headline(), dt.description(), dt.keywords());

        // 강한 / 약한 오행
        Element strong = chart.strongest();
        Element weak = chart.weakest();
        BalanceDto balance = new BalanceDto(
                strong.name(), Interpretation.ELEMENT.get(strong).strong(),
                weak.name(), Interpretation.ELEMENT.get(weak).weakTip(),
                Interpretation.REFLECTION.get(dm.element()));

        // 올해 운세
        Element yearElement = yearPillar.stem().element();
        Relation rel = Relation.between(dm.element(), yearElement);
        Interpretation.YearText yt = Interpretation.YEAR.get(rel);
        YearDto thisYear = new YearDto(currentSajuYear, yearPillar.korean(), yearPillar.hanja(),
                yearElement.name(), rel.koreanName(), rel.description(),
                yt.title(), yt.keywords(), yt.caution(), yt.body(), yt.action());

        return new ProfileResponse(p.getId(), p.getName(), p.getBirthDate(), p.getBirthTime(),
                p.getGender(), p.getBirthPlace(),
                new Saju(pillars, elements, core, balance, thisYear));
    }
}
