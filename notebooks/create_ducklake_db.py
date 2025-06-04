import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""### Install DuckLake""")
    return


@app.cell
def install_ducklake(mo):
    _df = mo.sql(
        f"""
        install ducklake;
        """
    )
    return


@app.cell
def creating_ducklake_database(mo):
    _df = mo.sql(
        f"""
        ATTACH 'ducklake:rb_ducklake.ducklake' AS rb_ducklake;
        USE rb_ducklake;
        """
    )
    return (rb_ducklake,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        CREATE TABLE nl_train_stations AS
            FROM 'https://blobs.duckdb.org/nl_stations.csv';
        """
    )
    return (nl_train_stations,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        FROM glob('rb_ducklake.ducklake.files/*');
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        FROM 'rb_ducklake.ducklake.files/*.parquet' LIMIT 10;
        """
    )
    return


@app.cell
def _(mo, nl_train_stations):
    _df = mo.sql(
        f"""
        UPDATE nl_train_stations SET name_long='Johan Cruijff ArenA' WHERE code = 'ASB';
        """
    )
    return


@app.cell
def _(mo, nl_train_stations):
    _df = mo.sql(
        f"""
        SELECT name_long FROM nl_train_stations WHERE code = 'ASB';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        FROM glob('rb_ducklake.ducklake.files/*');
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        FROM 'rb_ducklake.ducklake.files/ducklake-*-delete.parquet';
        """
    )
    return


@app.cell
def _(mo, rb_ducklake):
    _df = mo.sql(
        f"""
        FROM rb_ducklake.snapshots();
        """
    )
    return


@app.cell
def _(mo, nl_train_stations):
    _df = mo.sql(
        f"""
        SELECT name_long FROM nl_train_stations AT (VERSION => 1) WHERE code = 'ASB';
        """
    )
    return


@app.cell
def _(mo, nl_train_stations):
    _df = mo.sql(
        f"""
        SELECT name_long FROM nl_train_stations AT (VERSION => 2) WHERE code = 'ASB';
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        USE memory;
        DETACH rb_ducklake;
        """
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT version();
        """
    )
    return


if __name__ == "__main__":
    app.run()
