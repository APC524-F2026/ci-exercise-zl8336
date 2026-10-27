"""Run tests and build documentation in isolated environments."""

import nox

nox.needs_version = ">=2025.5.1"


@nox.session
def tests(session: nox.Session) -> None:
    """Install the test dependency group and run pytest."""
    pyproject = nox.project.load_toml("pyproject.toml")
    session.install(".", *nox.project.dependency_groups(pyproject, "test"))
    session.run("python", "-m", "pytest", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    """Build HTML and Markdown documentation, treating warnings as errors."""
    pyproject = nox.project.load_toml("pyproject.toml")
    session.install(".", *nox.project.dependency_groups(pyproject, "docs"))
    for builder in ("html", "markdown"):
        session.run(
            "sphinx-build",
            "-M",
            builder,
            "docs",
            "docs/_build",
            "-W",
            "--keep-going",
            *session.posargs,
        )
