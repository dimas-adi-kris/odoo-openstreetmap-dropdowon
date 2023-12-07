/** @odoo-module **/

import { AutoComplete } from "@web/core/autocomplete/autocomplete";
import { useChildRef } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";
import { CharField } from "@web/views/fields/char/char_field";
import { useInputField } from "@web/views/fields/input_field_hook";

import { useOSMAutocomplete } from "@custom_purchase/js/osm_autocomplete_core"

export class OSMAutoCompleteCharField extends CharField {
    setup() {
        super.setup();

        this.osm_autocomplete = useOSMAutocomplete();

        this.inputRef = useChildRef();
        useInputField({ getValue: () => this.props.value || "", parse: (v) => this.parse(v), ref: this.inputRef});
    }
    /**
     * Validates the input search term for a search operation.
     *
     * @param {string} request - The search term to be validated.
     * @returns {boolean} - `true` if the search term is valid (non-null string with a length greater than 2), `false` otherwise.
     *
     *
     */
    validateSearchTerm(request) {
        return request && request.length > 2;
    }

    get sources() {
        return [
            {
                options: async (request) => {
                    if (this.validateSearchTerm(request)) {
                        const suggestions = await this.osm_autocomplete.autocomplete(request);
                        suggestions.forEach((suggestion) => {
                            suggestion.classList = "osm_autocomplete_dropdown_char";
                        });
                        return suggestions;
                    }
                    else {
                        console.log("no suggestions");
                        return [];
                    }
                },
                optionTemplate: "custom_purchase.CharFieldDropdownOption",
                placeholder: _t('Searching Autocomplete test...'),
            },
        ];
    }

    async onSelect(option) {
        const data = await this.osm_autocomplete.getCreateData(Object.getPrototypeOf(option));
        this.props.record.update(data.address);
    }
}

OSMAutoCompleteCharField.template = "custom_purchase.OSMAutoCompleteCharField";
OSMAutoCompleteCharField.components = {
    ...CharField.components,
    AutoComplete,
};

registry.category("fields").add("field_osm_autocomplete", OSMAutoCompleteCharField);
