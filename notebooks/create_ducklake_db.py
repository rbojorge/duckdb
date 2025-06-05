import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Install ducklake

    https://ducklake.select/docs/stable/duckdb/introduction
    """
    )
    return


@app.cell
def install_ducklake(mo):
    _df = mo.sql(
        f"""
        install ducklake;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(f"""## Create a ducklake database or attach if exist""")
    return


@app.cell
def creating_ducklake_database(mo):
    _df = mo.sql(
        f"""
        -- "ducklake:ducklake/" indicate the path for the ducklake DB and parquet files
        ATTACH 'ducklake:ducklake/rb_ducklake.ducklake' AS rb_ducklake; -- (DATA_PATH 'ducklake/');
        USE rb_ducklake;
        """
    )
    return (rb_ducklake,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(f"""## Create tables and test ducklake feature in the rb_ducklake duckdb database""")
    return


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
def _():
    # variable with the ducklake duckdb database for use
    db = "ducklake/rb_ducklake"
    db
    return (db,)


@app.cell
def _(db, mo):
    _df = mo.sql(
        f"""
        FROM glob('{db}.ducklake.files/*');
        """
    )
    return


@app.cell
def _(db, mo):
    _df = mo.sql(
        f"""
        FROM '{db}.ducklake.files/*.parquet' LIMIT 10;
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
def _(db, mo):
    _df = mo.sql(
        f"""
        FROM glob('{db}.ducklake.files/*');
        """
    )
    return


@app.cell
def _(db, mo):
    _df = mo.sql(
        f"""
        FROM '{db}.ducklake.files/ducklake-*-delete.parquet';
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
def _(mo):
    version = mo.ui.slider(1, 30, label="Time travel")
    version
    return (version,)


@app.cell
def _(version):
    version.value
    return


@app.cell
def _(mo, nl_train_stations, version):
    _df = mo.sql(
        f"""
        SELECT name_long FROM nl_train_stations AT (VERSION => {version.value}) WHERE code = 'ASB';
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


@app.cell
def _():
    import marimo
    print(marimo.__version__)
    return


if __name__ == "__main__":
    app.run()
