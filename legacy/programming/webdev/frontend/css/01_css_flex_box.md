# CSS flex box techniques
Here we will see some techniques regarding flex box and how it display content of an `html` element.

# When flex box is called
- When the `flex box` is setted in an `html` element, the first thing it wil do is apply a `width: max-content` in all child elements. Interestingly enough, this desables line break, so if the content of the child element is too wide, it will bleed out of the parent content and even create side scrolling. So if you have a paragraph, it will not line break but it will break the page instead. But `flex box` know that. And differently from `width: max-content`, if the content is too wide, it will shrink the elements so that they can fit in the parent element, but just if the child element is too wide. 

- When you declare the width of a child element, flexbox will try to obey, but if things don't fit properly, it will shrink the elements to make it happen. It will try always to make the content fit. So, if your width setting makes spare space aside the content, it will be shrinked. If lines can be wrapped, they will be. But if the content is too wide, then it may bleed out the parent `flex` component. It is important to know that, flex will always shrink things by a constant rate. So the final widths will be proportional to what they would bi without the shrinking. And the way that it does it doesn't regard the padding and margin, so things can get pretty strange if you want things to have the same size. For that, Grid is recommended.

- Then it will default to the `flex-row` direction and will place the child elements in a horizontal line.

