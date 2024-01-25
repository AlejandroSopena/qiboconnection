""" Tests methods for job result """
import numpy as np

from qiboconnection.models.job_result import JobResult
from qiboconnection.typings.enums import JobType


def test_job_result_creation():
    """Test job result creation"""
    job_result = JobResult(
        job_id=1,
        http_response="gASVsAAAAAAAAACMFW51bXB5LmNvcmUubXVsdGlhcnJheZSMDF9yZWNvbnN0cnVjdJSTlIwFbnVtcHmUjAduZGFycmF5lJOUSwCFlEMBYpSHlFKUKEsBSwWFlGgDjAVkdHlwZZSTlIwCZjiUiYiHlFKUKEsDjAE8lE5OTkr_____Sv____9LAHSUYolDKAAAAAAAAPA_AAAAAAAA8D8AAAAAAADwPwAAAAAAAPA_AAAAAAAA8D-UdJRiLg==",
        job_type=JobType.CIRCUIT,
    )

    assert isinstance(job_result, JobResult)
    assert job_result.job_id == 1
    assert (
        job_result.http_response
        == "gASVsAAAAAAAAACMFW51bXB5LmNvcmUubXVsdGlhcnJheZSMDF9yZWNvbnN0cnVjdJSTlIwFbnVtcHmUjAduZGFycmF5lJOUSwCFlEMBYpSHlFKUKEsBSwWFlGgDjAVkdHlwZZSTlIwCZjiUiYiHlFKUKEsDjAE8lE5OTkr_____Sv____9LAHSUYolDKAAAAAAAAPA_AAAAAAAA8D8AAAAAAADwPwAAAAAAAPA_AAAAAAAA8D-UdJRiLg=="
    )
    assert (job_result.data == np.array([1.0, 1.0, 1.0, 1.0, 1.0])).all()


def test_job_result_qprogram_works():
    """Test we are rising exceptions to inform correctly that PROGRAMS are not currently supported."""

    job_result = JobResult(
        job_id=0,
        http_response="W3sicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNTEsICIxIjogMC40OX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY0OSwgIjEiOiAwLjM1MX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjU3MiwgIjEiOiAwLjQyOH19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjYzNywgIjEiOiAwLjM2M319LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY5MSwgIjEiOiAwLjMwOX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjcwOCwgIjEiOiAwLjI5Mn19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY4MSwgIjEiOiAwLjMxOX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY4NiwgIjEiOiAwLjMxNH19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY2NSwgIjEiOiAwLjMzNX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjcwNCwgIjEiOiAwLjI5Nn19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjYzOCwgIjEiOiAwLjM2Mn19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjYzLCAiMSI6IDAuMzd9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC43LCAiMSI6IDAuM319LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY5MywgIjEiOiAwLjMwN319LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjcwNSwgIjEiOiAwLjI5NX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY5MywgIjEiOiAwLjMwN319LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjcwNCwgIjEiOiAwLjI5Nn19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjY4OSwgIjEiOiAwLjMxMX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjczMiwgIjEiOiAwLjI2OH19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjcxLCAiMSI6IDAuMjl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MTcsICIxIjogMC4zODN9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NDUsICIxIjogMC4zNTV9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42OTcsICIxIjogMC4zMDN9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MzYsICIxIjogMC4zNjR9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NTEsICIxIjogMC4zNDl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NjYsICIxIjogMC4zMzR9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MzcsICIxIjogMC4zNjN9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MTksICIxIjogMC4zODF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC40NjIsICIxIjogMC41Mzh9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42OTksICIxIjogMC4zMDF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42ODYsICIxIjogMC4zMTR9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NjEsICIxIjogMC4zMzl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42OTksICIxIjogMC4zMDF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NzgsICIxIjogMC4zMjJ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MzksICIxIjogMC4zNjF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NzMsICIxIjogMC4zMjd9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NDEsICIxIjogMC4zNTl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42ODQsICIxIjogMC4zMTZ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NzMsICIxIjogMC4zMjd9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42ODUsICIxIjogMC4zMTV9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NTUsICIxIjogMC4zNDV9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC41ODQsICIxIjogMC40MTZ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NjksICIxIjogMC4zMzF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MSwgIjEiOiAwLjM5fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjM1LCAiMSI6IDAuMzY1fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjQ2LCAiMSI6IDAuMzU0fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjU1LCAiMSI6IDAuMzQ1fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjA0LCAiMSI6IDAuMzk2fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjM3LCAiMSI6IDAuMzYzfX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjQ1LCAiMSI6IDAuMzU1fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjY4LCAiMSI6IDAuMzMyfX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNywgIjEiOiAwLjN9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NTcsICIxIjogMC4zNDN9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC41OTQsICIxIjogMC40MDZ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MjMsICIxIjogMC4zNzd9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NjMsICIxIjogMC4zMzd9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42ODEsICIxIjogMC4zMTl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42OCwgIjEiOiAwLjMyfX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjc1LCAiMSI6IDAuMzI1fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjM1LCAiMSI6IDAuMzY1fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjQyLCAiMSI6IDAuMzU4fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNTksICIxIjogMC40MX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjYzLCAiMSI6IDAuMzd9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MzgsICIxIjogMC4zNjJ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NzIsICIxIjogMC4zMjh9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NTQsICIxIjogMC4zNDZ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MzgsICIxIjogMC4zNjJ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MjEsICIxIjogMC4zNzl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NDUsICIxIjogMC4zNTV9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NzEsICIxIjogMC4zMjl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC41MTEsICIxIjogMC40ODl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MDEsICIxIjogMC4zOTl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MjgsICIxIjogMC4zNzJ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MjgsICIxIjogMC4zNzJ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42MjEsICIxIjogMC4zNzl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NjksICIxIjogMC4zMzF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NDksICIxIjogMC4zNTF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NjksICIxIjogMC4zMzF9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC42NDcsICIxIjogMC4zNTN9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC40MjUsICIxIjogMC41NzV9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC41ODEsICIxIjogMC40MTl9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC41NywgIjEiOiAwLjQzfX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjIyLCAiMSI6IDAuMzc4fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjI0LCAiMSI6IDAuMzc2fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNTk0LCAiMSI6IDAuNDA2fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjE2LCAiMSI6IDAuMzg0fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjYxLCAiMSI6IDAuMzM5fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjU2LCAiMSI6IDAuMzQ0fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNTY0LCAiMSI6IDAuNDM2fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNTgyLCAiMSI6IDAuNDE4fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjMyLCAiMSI6IDAuMzY4fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjU3LCAiMSI6IDAuMzQzfX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjM2LCAiMSI6IDAuMzY0fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNTU2LCAiMSI6IDAuNDQ0fX0sIHsicHJvYmFiaWxpdGllcyI6IHsiMCI6IDAuNjYsICIxIjogMC4zNH19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjYzOCwgIjEiOiAwLjM2Mn19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjU1MSwgIjEiOiAwLjQ0OX19LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjYxMywgIjEiOiAwLjM4N319LCB7InByb2JhYmlsaXRpZXMiOiB7IjAiOiAwLjU0LCAiMSI6IDAuNDZ9fSwgeyJwcm9iYWJpbGl0aWVzIjogeyIwIjogMC41NjgsICIxIjogMC40MzJ9fV0=",
        job_type="qprogram",
    )
    assert isinstance(job_result.data, (dict | list))


def test_job_result_program_raises_error():
    """Test we are rising exceptions to inform correctly that PROGRAMS are not currently supported."""

    job_result = JobResult(job_id=0, http_response="WzAuMSwgMC4xLCAwLjEsIDAuMSwgMC4xXQ==", job_type="program")
    assert isinstance(job_result.data, str)