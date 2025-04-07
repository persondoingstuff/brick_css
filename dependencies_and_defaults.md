## Sizes

### Grid
Display child in a grid, with various size

- `[data-grid]`:
    - Set to size xs, sm, md, lg or xl.
    - Set 'expand' to auto-fit, and 'keep' to auto-fill.
- Adjust gap size with `[data-layout]`
- Properties with defaults that can be overriden:
    * `--brick-grid-min-size` - defaults to `18` (em, auto-converted)
    * `--brick-grid-min-pct` - defaults to `20` (pct, auto-converted)
    * `--brick-grid-mode` - defaults to `auto-fill`
    * `--brick-grid-spacing` - defaults to `--brick-block-spacing`


## Effects
* `--brick-outline-width` - defaults to `--brick-border-width`
* `--brick-scrollbar-width` - defaults to `0` - TODO: Not used anywhere yet

## Typography
Additional properties can be set to override defaults.

* Headings – properties can be set for each heading level, but by default most properties are shared (size being the only one set differently for each level)
    * `--brick-font-heading` - defaults to `--brick-font-main` - Applies to all levels
    * `--brick-line-length-headings` - defaults to `--brick-line-length-short` - Applies to all levels
    * `--brick-margin-after-headings` - defaults to `--brick-size-rel-xs` - Applies to all levels
    * `--brick-margin-before-headings` - defaults to `--brick-size-rel-md`
        * `--brick-margin-before-h1`, `--brick-margin-before-h2`, `--brick-margin-before-h3`, `--brick-margin-before-h4`, `--brick-margin-before-h5` and `--brick-margin-before-h6` - default to `--brick-margin-before-headings`
    * `--brick-font-weight-headings` - defaults to `--brick-font-weight-bold`
        * `--brick-font-weight-h1`, `--brick-font-weight-h2`, `--brick-font-weight-h3`, `--brick-font-weight-h4`, `--brick-font-weight-h5` and `--brick-font-weight-h6` - default to `--brick-font-weight-headings`
    * `--brick-line-height-headings` - defaults -to `--brick-line-height-tight`
        * `--brick-line-height-h1`, `--brick-line-height-h2`, `--brick-line-height-h3`, `--brick-line-height-h4`, `--brick-line-height-h5` and `--brick-line-height-h6` - default to `--brick-line-height-headings`
    * `--brick-font-color-h1` and `--brick-font-color-h2` - default to `--brick-color-headings-big`
    * `--brick-font-color-h3`, `--brick-font-color-h4`, `--brick-font-color-h5` and `--brick-font-color-h6`- default to `--brick-color-headings-small`
    * Sizes
        * `--brick-font-size-h1` - default to `--brick-size-fluid-xxl`
        * `--brick-font-size-h2` - default to `--brick-size-fluid-xl`
        * `--brick-font-size-h3` - default to `--brick-size-fluid-lg`
        * `--brick-font-size-h4` - default to `--brick-size-rel-xl`
        * `--brick-font-size-h5` - default to `--brick-size-rel-lg`
        * `--brick-font-size-h6` - default to `--brick-size-rel-md-lg`
* List
    * `--brick-list-style` - defaults to `square`
* Horizontal rule – by default a short centered line with a gray mid tone color. !!TODO support data-surface
    * `--brick-hr-spacing` - defaults to double of `--brick-typography-block-spacing`
    * `--brick-hr-color` - defaults to `--brick-color-accent-subtle`
    * `--brick-hr-thickness` - defaults to `--brick-border-width`
    * `--brick-hr-width` - defaults to `--brick-line-length-very-short`
* Blockquote -- by default a thick gray mid tone bar at the start of the line
    * `--brick-blockquote-spacing-block` - defaults to `--brick-typography-block-spacing`
    * `--brick-blockquote-spacing-inline` - defaults to double of `--brick-typography-block-spacing`
    * `--brick-blockquote-border-width` - defaults to `--brick-border-width-heavy`
    * `--brick-blockquote-border-color` - defaults to `--brick-color-accent-subtle`
    * `--brick-blockquote-footer-color` - defaults to `--brick-color-surface-2`
* Various colored elements - scope: `:where(:root, [data-theme], [data-surface])`
    * `--brick-code-color` - defaults to `--brick-color-content-active`
    * `--brick-code-background-color` - defaults to `--brick-color-shaded-bold`
    * `--brick-kbd-color` - defaults to `--brick-color-background-active`
    * `--brick-kbd-background-color` - defaults to `--brick-color-content-active`
    * `--brick-mark-background-color` - defaults to `--brick-color-warning-surface`
    * `--brick-mark-color` - defaults to `--brick-color-content-active`
    * `--brick-ins-color` - defaults to `--brick-color-success-content`
    * `--brick-del-color` - defaults to `--brick-color-danger-content`

## Elements

### Link

All link properties are set as overrideable defaults, except `--brick-link-color` and `--brick-link-color-active` which are defined on `:root`, `[data-theme]` and `[data-surface]`.

* Text
    * `--brick-link-font-weight` - defaults to `--brick-font-weight`

* Background – transparent by default
    * `--brick-link-background-color` - defaults to `transparent`
    * `--brick-link-background-color-active` - defaults to `--brick-link-background-color`
* Decoration – by default underline same color as text
    * `--brick-link-decoration` - defaults to `underline`
    * `--brick-link-decoration-active` - defaults to same as `--brick-link-decoration`
    * `--brick-link-decoration-color` - defaults to `--brick-link-color`
    * `--brick-link-decoration-color-active` - defaults to `--brick-link-color-active`
    * `--brick-link-decoration-offset` - defaults to `--brick-size-rel-xxs`
    * `--brick-link-decoration-offset-active` - defaults to same as `--brick-link-decoration-offset`
    * `--brick-link-decoration-thickness` - defaults to `from-font`
    * `--brick-link-decoration-thickness-active` - defaults to same as `--brick-link-decoration-thickness`

* Transition – off by default
    * `--brick-link-transition-duration` - defaults to `0`
    * `--brick-link-transition-mode` - defaults to `--brick-transition-mode`
    * `--brick-link-transition-properties` - defaults to `none`


### Button

Most button properties are set with overrideable defaults. Some use the general controls styling.

By default the background is the primary color, with light text. Color choices can be made using `[data-surface]`. Additionally,`[data-style]` can be set to `outline`.

* Width – by default at least 10 characters wide, and otherwise fitting content width
    * `--brick-button-width` - defaults to `fit-content` - could be set to eg. `100%`
    * `--brick-button-width-min` - defaults to `10ch`

* Padding – by default the standard padding for controls
    * `--brick-button-padding-inline` - defaults to `--brick-control-spacing-inline`
    * `--brick-button-padding-block` - defaults to `--brick-control-spacing-block`

* Text – by default light color text with regular weight
    * `--brick-button-text-color` - defaults to `--brick-color-content-contrast`
    * `--brick-button-text-color-active` - defaults to same as `--brick-button-text-color`
    * `--brick-button-text-weight` - defaults to `--brick-font-weight-regular`

* Background color
    * `--brick-button-background-color` - defaults to `--brick-color-primary-accent`
    * `--brick-button-background-color-active` - defaults to `--brick-color-primary-accent-bold`

* Border – by default same color as the background, with the global standard width and the border radius used for controls
    * `--brick-button-border-width` - defaults to `--brick-border-width`
    * `--brick-button-border-color` - defaults to same as background
    * `--brick-button-border-color-active` - defaults to same as background (active)
    * `--brick-button-border-rounding` - defaults to `--brick-control-border-rounding`
    * `--brick-button-border-rounding-active` - defaults to same as `--brick-button-border-rounding`

* Box shadow – off by default
    * `--brick-button-shadow` - defaults to `--brick-shadow-none`
    * `--brick-button-shadow-active` - defaults to `--brick-button-shadow`

* Transition – off by default, follows the setting for controls

This is the hierarchy for background and text color (from lowest to highest):

- When default when settings have been changed
    - Normal: primary accent background, with light text
    - Active: primary accent bold background, same text color as normal
- When default settings have been defined
    - Follow the settings, falls back to the above for anything that has not been defined
- When `data-surface` has been set, and not to surface 1, 2 or 3
    - Normal: surface setting, light text
    - Active: surface setting alt, same light text as normal
- When `data-surface` has been set to 1, 2 or 3
    - Normal: surface setting, content color for surface setting
    - Active: surface setting alt, content color for surface setting
- When `data-surface` has been set and `data-style` is set to `outline`
    - Normal: transparent background, text and border set to current surface setting
    - Active: transparent background, text and border set to current surface setting alt

### Table

* `--brick-table-background-color` - defaults to `--brick-color-background`
* `--brick-table-background-color-alt` - defaults to `--brick-table-background-color`, or `--brick-color-background-active` when striped
* `--brick-table-content-color` - defaults to `--brick-color-content-2`
* `--brick-table-divider-color` - defaults to `--brick-color-surface-3`, or `transparent` when striped
* `--brick-table-divider-width` - defaults to `--brick-border-width`

### Card
* `--brick-card-background-color` - defaults to `--brick-color-surface-2`
* `--brick-card-background-color-alt` -- defaults to `--brick-card-background-color`
* `--brick-card-border-color` - defaults to `--brick-card-background-color`
* `--brick-card-border-width` - defaults to `--brick-border-width`
* `--brick-card-border-rounding` - defaults to `--brick-border-rounding`
* `--brick-card-divider-color` - defaults to `--brick-card-border-color`
* `--brick-card-divider-width` - defaults to `--brick-card-border-width`
* `--brick-card-box-shadow` - defaults to `--brick-shadow-none`

### Accordion / details
* `--brick-accordion-content-color` - defaults to `--brick-color-content` - overridden by `--brick-active-style-content`
* `--brick-accordion-content-color-alt` - defaults to `--brick-color-content-active` - overridden by `--brick-active-style-content`
* `--brick-accordion-background-color` - defaults to `transparent` - overridden by `--brick-active-style-surface`
* `--brick-accordion-background-color-active` - defaults to same as `--brick-accordion-background-color` - overridden by `--brick-active-style-surface`
* `--brick-accordion-border-color` - defaults to same as `--brick-accordion-background-color` - overridden by `--brick-active-style-surface`
* `--brick-accordion-border-color-alt` - defaults to same as `--brick-accordion-background-color-active` - overridden by `--brick-active-style-surface`
* `--brick-accordion-border-width` - defaults to `0`
* `--brick-accordion-rounding` - defaults to `--brick-border-rounding-barely` - overridden by `--_card-rounding`


---

# Usages

--brick-form-disabled-opacity
	Used once, in check/radio disabled

--brick-form-element-width
	Used once, for general form elements

--brick-form-padding-inline
--brick-form-padding-block
	Used for general inputs and input height, dropdown details, file and color inputs

--brick-form-border-width
	Used for dropdown details, range thumb, general inputs and input height

--brick-form-control-border-width
	Used twice in one selector, for radio/check

--brick-form-control-size
	Used for check/radio, range

--brick-form-block-spacing + --brick-form-block-spacing-small
	Used for form itself, legend, label, small

--brick-control-border-rounding
	Used for dropdown details, button, general inputs, range, color input

--brick-form-color-*
	disabled + alt: used for check/radio, range, general inputs
	not used: brick-form-color-valid, brick-form-color-valid-alt, brick-form-color-invalid, brick-form-color-invalid-alt
		Should they be used for icons, validation text?

--brick-form-border-color*
	Used for general inputs, check/radio, dropdown details
	Redefined by surface

--brick-form-content-color + --brick-form-content-color-active
	Used for dropdown details, file input, general inputs, fallback in legend and label

--brick-form-background-color + --brick-form-background-color-active
	Used for dropdown details, general inputs, select

--brick-form-background-color-highlight + --brick-form-background-color-disabled
	Used for check/radio, range, general inputs
	Redefined by surface

--brick-form-accent*
	Used for general inputs, range, check/radio
	Redefined by surface

--brick-form-placeholder-color + --brick-form-placeholder-font-weight + --brick-form-placeholder-font-size + --brick-form-placeholder-opacity*
	Used for general input, select disabled

