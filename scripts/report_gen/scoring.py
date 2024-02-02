"""
This module contains a collection of functions for processing confusion
matrices and computing tool scores based on a scoring schema.
"""

from pathlib import Path
import logging
import json
import sys
import csv
import os


SCORING_SCHEMA_FILE_NAME = 'scoring_schema.json'


def get_scoring_schema() -> dict:
    """
    Retrieves the scoring schema from a JSON file and returns it as a
    dictionary.

    The function determines the path to the scoring schema file, loads the
    content from the JSON file, and returns it as a dictionary.
    """
    scoring_schema = {}

    # Get scoring schema path
    scoring_schema_dir_path = os.path.dirname(os.path.abspath(__file__))
    scoring_schema_path = Path(scoring_schema_dir_path).joinpath(SCORING_SCHEMA_FILE_NAME)

    try:
        # Load scoring schema
        with open(scoring_schema_path, 'r') as f:
            scoring_schema = json.load(f)

    except FileNotFoundError:
        logging.error(f'Scoring schema file not found: {scoring_schema_path}')
        sys.exit(1)

    except json.JSONDecodeError:
        logging.error(f'Error decoding the scoring schema file: {scoring_schema_path}')
        sys.exit(1)

    return scoring_schema


def compute_score(cm_path: str) -> int:
    """
    Computes the tool score based on a provided confusion matrix file.

    The scoring is determined using a predefined scoring schema retrieved
    through the get_scoring_schema() function. The schema assigns scores to
    different outcomes in the confusion matrix, and the total score is
    calculated based on the occurrences in the provided matrix file.
    """
    score = 0
    scoring_schema = get_scoring_schema()

    try:
        with open(cm_path, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)    # discard header

            for row in csv_reader:
                res = row[2]    # get result
                score += scoring_schema[res]

    except FileNotFoundError:
        logging.error(f'Confusion matrix file not found: {cm_path}')
        sys.exit(1)

    # Empty file
    except StopIteration:
        logging.error(f'The confusion matrix file "{cm_path}" is empty.')
        sys.exit(1)

    return score


def count_outcomes(cm_path: str) -> dict:
    """
    Counts the occurrences of each result in a CSV confusion matrix file.

    The function reads the provided CSV confusion matrix file and counts the
    occurrences of each unique result, returning a dictionary with the result
    as the key and its count as the value.
    """
    outcomes_count = {}

    try:
        with open(cm_path, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)

            for row in csv_reader:
                outcome = row[2]
                outcomes_count[outcome] = outcomes_count.get(outcome, 0) + 1

    except FileNotFoundError:
        logging.error(f'Confusion matrix file not found: {cm_path}')
        sys.exit(1)

    # Empty file
    except StopIteration:
        logging.error(f'The confusion matrix file "{cm_path}" is empty.')
        sys.exit(1)

    return outcomes_count


def compute_total_score(cm_paths: list) -> int:
    """
    Computes the total score based on a list of confusion matrix file paths.

    The function iterates through the provided list of confusion matrix file
    paths, computes the score for each file using the compute_score function,
    and sums up the individual scores to determine the total score.
    """
    total_score = 0

    for cm_path in cm_paths:
        total_score += compute_score(cm_path)

    return total_score


def count_total_outcomes(cm_paths: list) -> dict:
    """
    Counts the total number outcomes based on a list of confusion matrix file paths.

    The function iterates through the provided list of confusion matrix file
    paths, computes the outcome count for each file using the count_outcomes
    function, and aggregates the individual counts to determine the total count
    of each outcome.
    """
    outcomes_count = {}

    for cm_path in cm_paths:
        for outcome, count in count_outcomes(cm_path).items():
            outcomes_count[outcome] = outcomes_count.get(outcome, 0) + count

    return outcomes_count


def scoring_to_csv(results: dict) -> list:
    """
    Converts scoring results to a list of rows suitable for writing to a CSV file.

    The function takes a dictionary of scoring results for different tools and
    converts it into a format suitable for writing to a CSV file. Each row includes
    tool names, outcome counts based on the scoring schema, and the overall score.
    """
    scoring_schema = get_scoring_schema()
    header = ['tools'] + list(scoring_schema.keys()) + ['score']
    rows = [header]

    for tool, scores in results.items():
        tool_row = [tool]
        score, count = scores[0], scores[1]

        for outcome in scoring_schema:
            tool_row.append(count.get(outcome, 0))

        tool_row.append(score)
        rows.append(tool_row)

    return rows
