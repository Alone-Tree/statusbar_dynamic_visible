odoo.define('statusbar_dynamic_visible.statusbar_dynamic_visible', function (require) {
        "use strict";
        var relational_fields = require('web.relational_fields');
        relational_fields.FieldStatus.include({
            _setState: function () {
                var self = this;
                if (this.field.type === 'many2one') {
                    this.status_information = _.map(this.record.specialData[this.name], function (info) {
                        return _.extend({
                            selected: info.id === self.value.res_id,
                        }, info);
                    });
                } else {
                    var selection = this.field.selection;
                    if (this.attrs.statusbar_visible) {
                        var restriction = this.attrs.statusbar_visible;
                        if (this.attrs.dynamic_visible) {
                            var dynamic_state = this.attrs.dynamic_visible.split(",");
                            if (dynamic_state.indexOf(self.value) !== -1) {
                                restriction = restriction.replace('dynamic_state', self.value);
                            }
                        }
                        restriction = restriction.split(",");
                        selection = _.filter(selection, function (val) {
                            return _.contains(restriction, val[0]) || val[0] === self.value;
                        });
                    }
                    this.status_information = _.map(selection, function (val) {
                        return {id: val[0], display_name: val[1], selected: val[0] === self.value, fold: false};
                    });
                }
            },
        });
    }
);