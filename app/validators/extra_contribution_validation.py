from fastapi import HTTPException


def validate_extra_contribution(contributionValue, minValueExtraContributionValue):
    print(contributionValue, minValueExtraContributionValue)
    if contributionValue < minValueExtraContributionValue:
        raise HTTPException(
            status_code=400, detail=f"please note that the minimum contribution amount is {minValueExtraContributionValue}")