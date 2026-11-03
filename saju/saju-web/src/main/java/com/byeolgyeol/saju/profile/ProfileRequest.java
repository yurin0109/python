package com.byeolgyeol.saju.profile;

import jakarta.validation.constraints.*;

import java.time.LocalDate;
import java.time.LocalTime;

/** 사주 입력 폼 요청 */
public record ProfileRequest(
        @NotBlank(message = "이름을 입력해주세요.")
        @Size(max = 20, message = "이름은 20자 이내로 입력해주세요.")
        String name,

        @NotNull(message = "생년월일을 입력해주세요.")
        @PastOrPresent(message = "생년월일은 오늘 이전이어야 해요.")
        LocalDate birthDate,

        /** null 이면 시간 모름 */
        LocalTime birthTime,

        @NotBlank(message = "성별을 선택해주세요.")
        @Pattern(regexp = "[MF]", message = "성별 값이 올바르지 않아요.")
        String gender,

        @Size(max = 30)
        String birthPlace
) {
    @AssertTrue(message = "1900년 이후 생년월일만 계산할 수 있어요.")
    public boolean isSupportedYear() {
        return birthDate == null || birthDate.getYear() >= 1900;
    }
}
