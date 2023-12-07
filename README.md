# odoo-openstreetmap-dropdowon

Requirement :
- 
- Odoo 16
- Python 3.8 (or higher)


Things you need to know :
- 
- I build this from adapting contact company autofill which you can try using odoo community version. I remove unnecessary code and adapt it with my needed
- I use openstreetmap API which is still free to use as per 7 December 2023 (I don't know if in the future it still free or available)


How to install :
- 
- the core of this project is in the `custom_purchase/src`
- add 2 fields Char for `name` and `address`, 2 fields Float for `latitude` and `longitude`. This is the default that I make. You can custom as per you need. I'll show how to do it.
- in the form, add `widget="field_osm_autocomplete"` as attribute in address field

Concept :
-
It takes the result from `https://nominatim.openstreetmap.org/` as json and render it per option. For example, <a href="https://nominatim.openstreetmap.org/search?q=yogya&format=json">This link</a> will result a json with keyword `yogya`. You can custom your field in your model by following Custom Model.

Custom model :
- 
### Example 
You want to add `addresstype` from API into your model.
- add `addresstype` in your model
- in `src/osm_autocomplete_core.js` method `getCreateData`, add `'addresstype': address['addresstype'],` inside the result variable

bug is to be expected since I make it for my own needed. If you think my instruction is unclear or you think you can improve it, you can make `New Issue` and explain what confuse you from this project or fork this repository to impove this project. I will gladly help and update the repository