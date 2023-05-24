from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    file = {'title': "Maquinista", 'salary': '2000', 'type': "trainee"}
    fileTranslated = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert fileTranslated[0] == file
