# What is **HTML**?
Standing for Hyper Text Markup Language, the HTML is the standard markup language for creating Web pages. It describes the structure of the web page, telling to the web brownser what to show and how to display this content.

Here goes a minimal example:

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Page Title</title>
	</head>
	<body>

		<h1>My First Heading</h1>
		<p>My first paragraph.</p>

	</body>
</html>
```

In this example we can se that are **tags** and those are responsible for telling to the browser what each element is. It can be a **link**, a **paragraph** of pure text, a **header**, a **image** and other things. In this example we can se a `<!DOCTYPE html>` tag. This is responsible for specifying what is the html version that the page was written. In this case, "html" stands for the *HTML5* which is the newest, but other older versions could be used.

## The \<head\> TAG

The `<head> </head>` tag has important metadata that delivers some information about the page such as the title that appears in the browser tab (specified with the `<title></title>` tag). Other important metadata can be seen in the following example:

```html
<head>
	<!-- For characters set, viewport config and edge compatibility-->
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1.0, user-scalable=no">

	<!--! Stylesheet pointer -->
	<link rel="stylesheet" href="./assets/css/style.min.css">

	<!-- Page title -->
	<title>Felipe Ribeiro</title>
</head>
```

In this example we can se how to create comments in *HTML* code with the `<!-- -->` special tag. Other than that, we can see some interesting elements:

- `<meta http-equiv="X-UA-Compatible" content="ie=edge">` : To support *IE9* and *IE8* browsers. More info in https://stackoverflow.com/questions/6771258/what-does-meta-http-equiv-x-ua-compatible-content-ie-edge-do
- `<meta charset="utf-8">` : Define the charset for rendering the page. Necessary if you want to use accentuation or characters that aren't *ASCI*.
- `<meta name="viewport" content="width=device-width,  initial-scale=1.0, maximum-scale=1.0, user-scalable=no">`: Important to responsive websites that support mobile. It specifies some render parameters in cellphones. More info in https://www.geeksforgeeks.org/html-viewport-meta-tag-for-responsive-web-design/
- `	<link rel="stylesheet" href="./assets/css/style.min.css">` : References to files that may be important for the page. This can include stylesheets of css or javascript routines. So this tag declares external resources.

## The \<body\> TAG

The content that compose the page goes in the `<body> </body>` tag. It has everything that will be rendered in the page. some importante content *tag*s are:

- `<h1></h1>`, `<h2></h2>`, `<h3></h3>`... : Headers and subheaders. They are text that are more flashy. Probably is a title of some sort or big text that goes somewhere.
- `<p><\p>` : The default text object. Ready to populate the page with tons of information.
- `<img src="" alt="">`: Image tag. This is interesting as it doesn't have a closing tag. Some tags are like this, self contained. The src can lead to a *URL* or a *PATH* to a file (the image file of course) and the `alt` parameter is the floating text that appear when you hold the mouse over the image. It can be important as an accessibility tool.
- `<a href=""> </a>`: The link tag. With this tag one can create links to other pages inserting an url in the `href` parameter, or you can reference elements of the page inserting `"#hello"` as parameter, being "hello" a `id` of other html element. Any html tag in the body can have an `id`, it just a metter of deffining it (`<h1 id="hello"></h1>`). The text, image, paragraph or other element that goes inside the `<a></a>` tag becomes the clickable link.

You can create a bullet point list too, with the `<ul></ul>` tag, as follows:

```html
<ul>
  <li>good morning</li>
  <li>bom dia</li>
  <li>bone matin</li>
  <li>buenos dias</li>
</ul>
```

Is common practice to remove the decorators of the bullet points and use this structure to create menus in the website. And you can create a ordered list (enumerated) just using `<ol></ol>` substituting the `<ul></ul>` list.


