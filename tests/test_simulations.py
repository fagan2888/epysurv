import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from epysurv.simulation import PointSource, SeasonalNoise


def load_simulations(filepath):
    simulations = pd.read_csv(
        filepath, index_col=0, parse_dates=True, infer_datetime_format=True
    )
    return simulations


@pytest.mark.parametrize("SimulationAlgo", [PointSource, SeasonalNoise])
def test_simulate_outbreaks(SimulationAlgo, shared_datadir):
    """Test against changes in simulation behavior."""
    simulation_model = SimulationAlgo(seed=1)
    simulated = simulation_model.simulate(length=100, state_weight=1)
    saved_simulation = load_simulations(
        shared_datadir / f"{SimulationAlgo.__name__}_simulation.csv"
    )
    assert_frame_equal(simulated, saved_simulation)


@pytest.mark.parametrize("SimulationAlgo", [PointSource, SeasonalNoise])
def test_simulation_model_format(SimulationAlgo):
    simulation_model = SimulationAlgo()
    simulated = simulation_model.simulate(length=1)
    assert "n_cases" in simulated.columns
    assert "n_outbreak_cases" in simulated.columns