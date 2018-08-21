# Programming languages case styles

Different languages prefer different naming conventions and different letter case styles. I knew about the CamelCase, and in my University, I did work on a small project in Lisp, I didn't know about the `lisp-cas` or the `kebab-case`. I read it on a Github comment and found out what it means. Here are the three most widely used case categories:

## CamelCase
  Commonly used in Java and C#. 
  
  `TheQuickBrownFoxJumpsOverTheLazyDog`
  
   Spaces and punctuation are removed and the first letter of each word is capitalised. If this includes the first letter of the first word ("CamelCase", "PowerPoint", "TheQuick...", etc.), the case is sometimes called upper camel case (or, illustratively, CamelCase), Pascal case, or bumpy case. When the first letter of the first word is lowercase ("iPod", "eBay", "theQuickBrownFox..."), the case is usually known as lower camel case (illustratively: camelCase).

## Snake_case

  `The_quick_brown_fox_jumps_over_the_lazy_dog`
    
   Punctuation is removed and spaces are replaced by single underscores. Normally the letters share the same case (e.g. "UPPER_CASE_EMBEDDED_UNDERSCORE" or "lower_case_embedded_underscore") but the case can be mixed, as in OCaml modules. The style may also be called pothole case, especially in Python programming, in which this convention is often used for naming variables. Illustratively, it may be rendered snake_case, pothole_case, etc. When all-upper-case, it may be referred to as screaming snake case (or SCREAMING_SNAKE_CASE).

## kebab-case

  `The-quick-brown-fox-jumps-over-the-lazy-dog`
  
   Similar to snake case, above, except hyphens rather than underscores are used to replace spaces. It is also known as spinal case, Lisp case, and dash case (or illustratively as kebab-case) If every word is capitalised, the style is known as train case (TRAIN-CASE).
   
   Definitions from [Letter case (Wikipedia)](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles).
