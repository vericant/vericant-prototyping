var Handlebars = require('handlebars');

/**
 * Loads the corresponding partial
 * @param {String} partial - The partial name.
 * @param {Object} options - Handlebars object.
 * @example
 * {{partial 'test1'}}
 * @returns {String} compiled partial
 */

module.exports = function(partial, options) {
  var html = Handlebars.partials[partial];

  if (html === undefined) {
    return 'blah';
  }

  return html;
};
