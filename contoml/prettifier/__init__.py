from . import anontableindent, tableindent, tableassignment

"""
    TOMLFile prettifiers

    Each prettifier is a function that accepts the list of Element instances that make up the
    TOMLFile and it is allowed to modify it as it pleases.
"""


UNIFORM_TABLE_INDENTATION = tableindent.table_entries_should_be_uniformly_indented
UNIFORM_TABLE_ASSIGNMENT_SPACING = tableassignment.table_assignment_spacing
ANONYMOUS_TABLE_INDENTATION = anontableindent.anon_table_indent


ALL = (
    UNIFORM_TABLE_INDENTATION,
    UNIFORM_TABLE_ASSIGNMENT_SPACING,
    ANONYMOUS_TABLE_INDENTATION,
)


def prettify(toml_file, prettifiers=ALL):
    """
    Prettifies a TOMLFile instance according to pre-defined set of formatting rules.
    """
    for prettifier in prettifiers:
        prettifier(toml_file)