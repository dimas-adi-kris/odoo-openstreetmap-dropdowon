/** @odoo-module **/

import { loadJS } from "@web/core/assets";
import { _t } from "@web/core/l10n/translation";
import { KeepLast } from "@web/core/utils/concurrency";
import { useService } from "@web/core/utils/hooks";
import { renderToMarkup } from "@web/core/utils/render";
import { getDataURLFromFile } from "@web/core/utils/urls";

/**
 * Get list of companies via Autocomplete API
 *
 * @param {string} value
 * @returns {Promise}
 * @private
 */
export function useOSMAutocomplete() {
    const http = useService("http");
    const notification = useService("notification");
    const orm = useService("orm");

    async function autocomplete(value) {
        value = value.trim();

        let clearbitSuggestions = [];

        const clearbitPromise = await getClearbitSuggestions(value);
        clearbitPromise.forEach((suggestions) => {
            suggestions['label'] = suggestions['display_name'];
            suggestions['description'] = `Coordinate : ${suggestions['lat']} , ${suggestions['lon']}`;
        });
        clearbitSuggestions = clearbitPromise;
        return clearbitSuggestions;
    }

    /**
     * Get enriched data + logo before populating partner form
     *
     * @param {Object} company
     * @returns {Promise}
     */
    function getCreateData(address) {
        const removeUselessFields = (address) => {
            // Delete attribute to avoid "Field_changed" errors
            let result = {
                'name': address['name'],
                'address': address['display_name'],
                'latitude': parseFloat(address['lat']),
                'longitude': parseFloat(address['lon']),
            };
            return result;
        };
        return { address:removeUselessFields(address) };
    }


    /**
     * Use OpenStreetMap API to return suggestions
     *
     * @param {string} value
     * @returns {Promise}
     * @private
     */
    async function getClearbitSuggestions(value) {
        const url = `https://nominatim.openstreetmap.org/search?q=${value}&format=json`;
        try {
            const response = await http.get(url);
            return response; // Assuming response is an array of suggestions
        } catch (error) {
            console.error("Error in getClearbitSuggestions:", error);
            return [];
        }
    }

    return { autocomplete, getCreateData };
}
