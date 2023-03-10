from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort', 'file_name')

class RequestScema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()

    @validates_schema
    def check_all_cmd_valid(self, values: dict[str, str], *args, **kwargs):
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestScema, many=True)
    file_name = fields.Str(required=True)
