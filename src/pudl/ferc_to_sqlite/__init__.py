"""Dagster definitions for the FERC to SQLite process."""
import importlib.resources

from dagster import Definitions, graph

import pudl
from pudl.extract.ferc import ALL_DBF_EXTRACTORS
from pudl.extract.ferc1 import Ferc1DbfExtractor
from pudl.extract.ferc2 import Ferc2DbfExtractor
from pudl.extract.ferc6 import Ferc6DbfExtractor
from pudl.extract.ferc60 import Ferc60DbfExtractor
from pudl.extract.xbrl import xbrl2sqlite_op_factory
from pudl.resources import RuntimeSettings, datastore, ferc_to_sqlite_settings
from pudl.settings import EtlSettings, XbrlFormNumber

logger = pudl.logging_helpers.get_logger(__name__)


@graph
def ferc_to_sqlite():
    """Clone the FERC FoxPro databases and XBRL filings into SQLite."""
    for extractor in ALL_DBF_EXTRACTORS:
        extractor.get_dagster_op()()
    for form in XbrlFormNumber:
        xbrl2sqlite_op_factory(form)()


@graph
def ferc_to_sqlite_dbf_only():
    """Clone the FERC FoxPro databases into SQLite."""
    for extractor in ALL_DBF_EXTRACTORS:
        extractor.get_dagster_op()()


@graph
def ferc_to_sqlite_xbrl_only():
    """Clone the FERC XBRL databases into SQLite."""
    for form in XbrlFormNumber:
        xbrl2sqlite_op_factory(form)()


default_resources_defs = {
    "ferc_to_sqlite_settings": ferc_to_sqlite_settings,
    "runtime_settings": RuntimeSettings(),
    "datastore": datastore,
}

ferc_to_sqlite_full = ferc_to_sqlite.to_job(
    resource_defs=default_resources_defs,
    name="ferc_to_sqlite_full",
)

ferc_to_sqlite_fast_settings = EtlSettings.from_yaml(
    importlib.resources.files("pudl.package_data.settings") / "etl_fast.yml"
).ferc_to_sqlite_settings

ferc_to_sqlite_fast = ferc_to_sqlite.to_job(
    resource_defs=default_resources_defs,
    name="ferc_to_sqlite_fast",
    config={
        "resources": {
            "ferc_to_sqlite_settings": {
                "config": ferc_to_sqlite_fast_settings.model_dump(),
            },
            "runtime_settings": {
                "config": {},
            },
        },
    },
)

defs: Definitions = Definitions(jobs=[ferc_to_sqlite_full, ferc_to_sqlite_fast])
"""A collection of dagster assets, resources, IO managers, and jobs for the FERC to
SQLite ETL."""
