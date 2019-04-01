import os


def _is_surrounded_by(string, char):
    return (
        len(string) > 1
        and string[0] == string[-1] == char
    )


def _parse_file(env_file):

    env_config = dict()

    if not os.path.isfile(env_file):
        raise FileNotFoundError(f"Error: The file [ {env_file} ] does not exist.")

    with open(env_file, 'r') as fp:
        variables = fp.readlines()

    for var in variables:
        key, val = var.rsplit('=', 2)
        if _is_surrounded_by(val, '"') or _is_surrounded_by(val, "'"):
            val = val[1:-1]
        else:
                val = val.strip()

        env_config[key] = val

    return env_config


class ConfigEnvironment(object):

    def __init__(self, env_file):
        self.env_file = env_file
        self._dict = _parse_file(env_file)

    def load_environment(self):
        """
        Load the current dotenv as system environemt variable.
        """
        try:

            for k, v in self._dict.items():
                if k in os.environ:
                    continue

                os.environ[k] = v  # type: ignore
        except Exception as e:
            raise e

        return True

    def unload_environment(self):
        """
        Unload the current dotenv as system environemt variable.
        """
        try:

            for k, v in self._dict.items():
                if k in os.environ:
                    del os.environ[k]
            return True
        except Exception as e:
            raise e





