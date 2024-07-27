/** @type {import('eslint').Linter.FlatConfig} */
const config = [
  {
    files: ['*.js'],
    languageOptions: {
      ecmaVersion: 2021,
    },
    plugins: ['import'],
    rules: {
      // Add rules directly here or load from plugins
    },
    settings: {
      'import/resolver': {
        node: {
          extensions: ['.js'],
        },
      },
    },
  },
];

module.exports = config;
