import pytest
from src.scrubber import PIIScrubber

@pytest.fixture
def scrubber():
    return PIIScrubber()

def test_scrub_email(scrubber):
    text = "Contact me at anita.fake@gmail.com please."
    result = scrubber.scrub(text)
    assert "[EMAIL]" in result['scrubbed_text']
    assert "anita.fake@gmail.com" not in result['scrubbed_text']

def test_scrub_phone_simple(scrubber):
    text = "Call +61 412 345 678 now."
    result = scrubber.scrub(text)
    assert "[PHONE]" in result['scrubbed_text']
    assert "412 345 678" not in result['scrubbed_text']

def test_preserve_health_data(scrubber):
    # CRITICAL: Steps and BP should NOT be scrubbed
    text = "Steps today: 6234. BP 120/80."
    result = scrubber.scrub(text)
    assert "Steps today: 6234" in result['scrubbed_text']
    assert "BP 120/80" in result['scrubbed_text']
    assert "[PHONE]" not in result['scrubbed_text']

def test_scrub_name_context(scrubber):
    text = "Appointment with Dr. Kavita Rao tomorrow."
    result = scrubber.scrub(text)
    assert "[NAME]" in result['scrubbed_text']
    assert "Kavita Rao" not in result['scrubbed_text']

def test_overlap_handling(scrubber):
    text = "Ref ID: APPT-839201"
    result = scrubber.scrub(text)
    assert "[REF_ID]" in result['scrubbed_text']
    assert "APPT-839201" not in result['scrubbed_text']