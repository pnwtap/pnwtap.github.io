import pytest
from pnwtap.sheet import Location
from pnwtap.images import localize_images


def _loc(name, image):
    return Location(name, "poi", "hard", [(47.6, -122.3)], image, "")


def test_downloads_and_maps_images(tmp_path):
    calls = []

    def fake_download(url):
        calls.append(url)
        return b"\x89PNG-fake-bytes", "image/png"

    locs = [_loc("A", None), _loc("B", "http://x/b.png")]
    mapping = localize_images(locs, tmp_path, download=fake_download)

    assert 0 not in mapping                    # no image
    assert mapping[1].startswith("img/")
    assert mapping[1].endswith(".png")
    assert (tmp_path / "img" / mapping[1].split("/")[1]).read_bytes() == b"\x89PNG-fake-bytes"
    assert calls == ["http://x/b.png"]


def test_caches_by_url(tmp_path):
    calls = []

    def fake_download(url):
        calls.append(url)
        return b"data", "image/jpeg"

    locs = [_loc("B", "http://x/b.jpg")]
    localize_images(locs, tmp_path, download=fake_download)
    localize_images(locs, tmp_path, download=fake_download)   # second run
    assert calls == ["http://x/b.jpg"]         # downloaded only once


def test_download_failure_names_location(tmp_path):
    def boom(url):
        raise RuntimeError("404")

    with pytest.raises(ValueError, match="Fremont"):
        localize_images([_loc("Fremont", "http://x/none.jpg")], tmp_path, download=boom)
