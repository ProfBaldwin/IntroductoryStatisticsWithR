from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util.docutils import SphinxDirective


class ExampleNum(SphinxDirective):

    def run(self):
        env = self.env
        example_id = env.new_serialno('examplenum') + 1
        example_sect = nodes.section()
        example_sect['ids'] = "Example"
        label = "Example {number}".format(number = example_id)
        example_sect += nodes.title(text=label)
        return [example_sect]


def setup(app):
    app.add_directive("examplenum", ExampleNum)

    return {
            'version': '0.1',
            'parallel_read_safe': True,
            'parallel_write_safe': True,
            }


