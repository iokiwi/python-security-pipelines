# Pipelines for Securing your Python Development Lifecycle

Reference Repository from my Talk of the same title: [Pipelines for Securing your Python Development Lifecycle](https://docs.google.com/presentation/d/1hAYnZCIoPdgXLpZZsllKrhdKLscPrzpcAvUV5jrD8R4/edit?usp=sharing
)

Important files/directories/links

 * [samples](samples/) - Contains samples of things that will cause the pipelines to fail
 * [.gitlab-ci.yml](.gitlab-ci.yml) - Source code for the security pipelines

You can see the results of the pipeline here: 
https://gitlab.com/iokiwi/python-security-pipelines/-/pipelines

Please feel free to fork this repo and try it yourself. 

## Running tools locally
All of these tools can be run locally as well

Try with [uvx](https://docs.astral.sh/uv/getting-started/installation/):

 * `uvx bandit -x .venv -r .`
 * `uvx pip-audit -r samples/requirements.txt`

Gitleaks

  1. [Install gitleaks](https://github.com/gitleaks/gitleaks?tab=readme-ov-file#installing)
  2. `gitleaks git --verbose --redacted .`

## Have a play with the malicious yaml

```bash
uv run samples/naughty_yaml.py
```

More reading and examples: [YAML Deserialization Attack in Python](https://net-square.com/yaml-deserialization-attack-in-python.html)


## TODOs and Possible Enrichments

 * Translate it to Github actions as well
 * Share some other usefull scripts for CI
