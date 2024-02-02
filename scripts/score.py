from pathlib import Path
import argparse
import utils
from report_gen.scoring import (compute_total_score,
                                count_total_outcomes,
                                scoring_to_csv)


SOLCMC_Z3_CM_PATTERN = 'solcmc/build/z3/cm.csv'
SOLCMC_ELD_CM_PATTERN = 'solcmc/build/eld/cm.csv'
CERTORA_CM_PATTERN = 'certora/build/cm.csv'
SCORES_FILE_NAME = 'scores.csv'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir',
                        '-d',
                        help='Directory with CMs.',
                        required=True)
    parser.add_argument('--output',
                        '-o',
                        help='Output directory.',
                        required=True)
    args = parser.parse_args()

    # Dict to store scoring results
    results = {
            'solcmc-z3': (0, {}),
            'solcmc-eld': (0, {}),
            'certora': (0, {})
            }

    # Find the list of confusion matrices for every tool
    solcmc_z3_cm_paths = utils.find_paths_with_subpath(args.dir, SOLCMC_Z3_CM_PATTERN)
    solcmc_eld_cm_paths = utils.find_paths_with_subpath(args.dir, SOLCMC_ELD_CM_PATTERN)
    certora_cm_paths = utils.find_paths_with_subpath(args.dir, CERTORA_CM_PATTERN)

    # Compute and store the score and number of outcomes
    results['solcmc-z3'] = (compute_total_score(solcmc_z3_cm_paths),
                            count_total_outcomes(solcmc_z3_cm_paths))
    results['solcmc-eld'] = (compute_total_score(solcmc_eld_cm_paths),
                             count_total_outcomes(solcmc_eld_cm_paths))
    results['certora'] = (compute_total_score(certora_cm_paths),
                          count_total_outcomes(certora_cm_paths))

    # Convert results dict to csv
    csv_rows = scoring_to_csv(results)
    output_path = Path(args.output).joinpath(SCORES_FILE_NAME)
    utils.write_csv(output_path, csv_rows)

    print(f'Scores available in "{output_path}".')
