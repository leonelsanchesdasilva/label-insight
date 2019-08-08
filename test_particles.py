import pytest
import particles

def test_invalid_speed():
    with pytest.raises(ValueError) as info:
        particles.animate("wrong", "...")
    assert "integer value" in str(info.value)

def test_positive_speed():
    with pytest.raises(ValueError) as info:
        particles.animate(-1, "...")
    assert "greater than zero" in str(info.value)

def test_invalid_chamber_size():
    with pytest.raises(ValueError) as info:
        particles.animate(1, "")
    assert "should not be empty" in str(info.value)

def test_empty_chamber():
    results = particles.animate(1, "...")
    assert len(results) == 1
    assert results[0] == "..."

def test_very_fast_particles():
    results = particles.animate(10, "RLRLRLRLRL")
    assert len(results) == 2
    assert results[0] == "XXXXXXXXXX"
    assert results[1] == ".........."

def test_one_right_particle():
    results = particles.animate(2, "..R....")
    assert len(results) == 4
    assert results[0] == "..X...."
    assert results[1] == "....X.."
    assert results[2] == "......X"
    assert results[3] == "......."

def test_5_particles():
    results = particles.animate(3, "RR..LRL")
    assert len(results) == 4
    assert results[0] == "XX..XXX"
    assert results[1] == ".X.XX.."
    assert results[2] == "X.....X"
    assert results[3] == "......."

def test_8_particles():
    results = particles.animate(2, "LRLR.LRLR")
    assert len(results) == 5
    assert results[0] == "XXXX.XXXX"
    assert results[1] == "X..X.X..X"
    assert results[2] == ".X.X.X.X."
    assert results[3] == ".X.....X."
    assert results[4] == "........."

def test_complex_case():
    results = particles.animate(1, "LRRL.LR.LRR.R.LRRL.")
    assert len(results) == 19
    assert results[0] == "XXXX.XX.XXX.X.XXXX."
    assert results[1] == "..XXX..X..XX.X..XX."
    assert results[2] == ".X.XX.X.X..XX.XX.XX"
    assert results[3] == "X.X.XX...X.XXXXX..X"
    assert results[4] == ".X..XXX...X..XX.X.."
    assert results[5] == "X..X..XX.X.XX.XX.X."
    assert results[6] == "..X....XX..XX..XX.X"
    assert results[7] == ".X.....XXXX..X..XX."
    assert results[8] == "X.....X..XX...X..XX"
    assert results[9] == ".....X..X.XX...X..X"
    assert results[10] == "....X..X...XX...X.."
    assert results[11] == "...X..X.....XX...X."
    assert results[12] == "..X..X.......XX...X"
    assert results[13] == ".X..X.........XX..."
    assert results[14] == "X..X...........XX.."
    assert results[15] == "..X.............XX."
    assert results[16] == ".X...............XX"
    assert results[17] == "X.................X"
    assert results[18] == "..................."