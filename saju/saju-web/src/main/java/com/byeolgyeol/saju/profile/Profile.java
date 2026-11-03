package com.byeolgyeol.saju.profile;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

/**
 * 사주 프로필 (DB 테이블: profile)
 * clientId: 로그인 대신 브라우저마다 발급한 고유 ID로 "내 사주"를 구분한다.
 */
@Entity
@Table(name = "profile", indexes = @Index(name = "idx_profile_client", columnList = "client_id"))
public class Profile {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "client_id", nullable = false, length = 36)
    private String clientId;

    @Column(nullable = false, length = 20)
    private String name;

    @Column(name = "birth_date", nullable = false)
    private LocalDate birthDate;

    /** 태어난 시간을 모르면 null */
    @Column(name = "birth_time")
    private LocalTime birthTime;

    /** M / F */
    @Column(nullable = false, length = 1)
    private String gender;

    @Column(name = "birth_place", length = 30)
    private String birthPlace;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    protected Profile() {}

    public Profile(String clientId, String name, LocalDate birthDate, LocalTime birthTime,
                   String gender, String birthPlace) {
        this.clientId = clientId;
        update(name, birthDate, birthTime, gender, birthPlace);
    }

    @PrePersist
    void onCreate() {
        this.createdAt = LocalDateTime.now();
    }

    public void update(String name, LocalDate birthDate, LocalTime birthTime,
                       String gender, String birthPlace) {
        this.name = name;
        this.birthDate = birthDate;
        this.birthTime = birthTime;
        this.gender = gender;
        this.birthPlace = birthPlace;
    }

    public Long getId() { return id; }
    public String getClientId() { return clientId; }
    public String getName() { return name; }
    public LocalDate getBirthDate() { return birthDate; }
    public LocalTime getBirthTime() { return birthTime; }
    public String getGender() { return gender; }
    public String getBirthPlace() { return birthPlace; }
    public LocalDateTime getCreatedAt() { return createdAt; }
}
