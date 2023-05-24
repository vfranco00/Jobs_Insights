from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            list = []
            data = csv.DictReader(file)
            for item in data:
                list.append(item)
            return list

    except FileNotFoundError:
        raise Exception('Arquivo não foi encontrado')


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    try:
        return {job['job_type'] for job in read(path)}

    except FileNotFoundError:
        raise Exception('Arquivo não encontrado')


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    try:
        return [column for column in jobs if column['job_type'] == job_type]

    except FileNotFoundError:
        raise Exception('Arquivo não foi encontrado')
