#=================== new script =========================

# Example (using Tornado database module)
# After init (e.g. db = Database()) you will get all meta info about tables stored in db.meta attribute

from tornado import database

class Database:

    def __init__(self):

        self.database = database.Connection('localhost', 'mydb', 'root', '12345')
        self.meta = self.get_db_meta() # getting meta information about databse tables

    def get_db_meta(self):

        """ Pulls out meta information about database. """

        meta = dict() # empty meta container
        # getting tables
        tables = self.database.query('SHOW TABLES')
        # parsing tables list of dictionaries
        tables = [table.values()[0] for table in tables]
        for table in tables:
            meta[table] = self._get_table_meta(table)
        return meta

    def _get_table_meta(self, table):

        """ @type table str
            @return dict

            Pulls out meta information from database table.
        """

        # gathered metadata container
        gathered_meta = dict()
        # getting unparsed metadata
        unparsed_meta = self.database.query('SHOW COLUMNS FROM %s' % table)
        # parsing meta
        for meta in unparsed_meta:
            gathered_meta[meta.Field] = {
                'extra': meta.Extra if meta.Extra else None,
                'default': meta.Default if meta.Default else None,
                'key': meta.Key if meta.Key else None,
                'null': True if meta.Null == 'YES' else False,
                'type': self._meta_field_type(meta.Type)
            }
        return gathered_meta

    def _meta_field_type(self, type):

        """ @type type str
            @return str

            Translates SQL representation of field type into python data type.
        """

        regexs = {
            # reals
            'tinyint': {'re': re.compile(r'\btinyint\b'), 'type': 'int'},
            'smallint': {'re': re.compile(r'\bsmallint\b'), 'type': 'int'},
            'int': {'re': re.compile(r'\bint\b'), 'type': 'int'},
            'mediumint': {'re': re.compile(r'\bmediumint\b'), 'type': 'int'},
            'bigint': {'re': re.compile(r'\bbigint\b'), 'type': 'int'},
            # floats
            'float': {'re': re.compile(r'\bfloat\b'), 'type': 'float'},
            'double': {'re': re.compile(r'\bdouble\b'), 'type': 'float'},
            'decimal': {'re': re.compile(r'\bdecimal\b'), 'type': 'float'}
            # if none of previous regexes matches then we have a string
        }

        for regex in regexs.values():
            if bool(regex['re'].search(type)):
                return regex['type']
        return 'str'

