# Css measure units
In css we must define the size of things with a set of measurement units. Those can be absolute references o relative references.

## Absolute references
The absolute references don't change, that is, they are not based in anything. Always assuming the same size.

unity | definition
-|-
cm| Centimeters
mm| milimetres
Q | Quarter-milimetres
in| inches
pc| picas
pt| points
px| pixels

From those the only one that is common is the `px` for web development. The `cm` unit measure is used more for printing, for example.

## Relative references
The relative ones depend on something. They can change in function of this dependent variable. This is good for reactive interfaces that can adapt to various screen sizes. So there are lots of units relative to the screen size.
The relative units are the following:

unity | definition
-|-
em   | Based on the `font-size` of parent.
ex   | `x-height` of the element's font.
ch   | The measure of the width of `0` character on the elemtnt's font. 
rem  | Dependent on the font size of the root element.
lh   | Line height of the element.
vw   | `1%` of the width of the viewport.
vh   | `1%` of the height of the viewport.
vmin | `1%` of the size of the smaller viewport dimension.
vmax | `1%` of the size of the bigger viewport dimension.
%    | Literal percentage of the same value of parent.

## Reactiveness
If the width is too small, text will try to wrap to fit in int.
