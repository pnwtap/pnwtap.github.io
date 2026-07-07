from pnwtap import config


def test_scoring_maxes_at_1000():
    assert len(config.RAMP) == len(config.MULTIPLIERS)
    assert 100 * sum(config.MULTIPLIERS) == 1000


def test_ramp_uses_valid_difficulties():
    assert set(config.RAMP) <= {"easy", "medium", "hard"}
    assert set(config.EMOJI) == {"easy", "medium", "hard"}
