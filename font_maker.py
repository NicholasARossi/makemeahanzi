import pandas as pd


X_ADVANCE = 1000
HEADER = """<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd" >

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">

<metadata>

</metadata>
<defs>
<font id="danxianziti SVG" horiz-adv-x="378" >
<font-face
font-family="danxianziti SVG"
units-per-em="1000"
ascent="800"
descent="-200"
cap-height="500"
x-height="300"
/>
"""
ENGLISH_CHARECTERS="""
<glyph unicode=" " glyph-name="space" horiz-adv-x="378" />
<glyph unicode="!" glyph-name="exclam" horiz-adv-x="173" d="M 167 630 L 167 164 M 148 22.1 L 148 -12.6 L 186 -12.6 L 183 22.1 L 148 22.1" />
<glyph unicode="&#x22;" glyph-name="quotedbl" horiz-adv-x="331" d="M 126 624 L 126 517 M 271 624 L 271 517" />
<glyph unicode="#" glyph-name="numbersign" horiz-adv-x="709" d="M 362 624 L 151 -25.2 M 680 627 L 466 -22.1 M 107 454 L 753 454 M 81.9 164 L 721 164" />
<glyph unicode="$" glyph-name="dollar" horiz-adv-x="706" d="M 110 101 L 110 56.7 L 161 6.3 L 652 6.3 L 706 63 L 706 255 L 649 312 L 164 312 L 113 362 L 113 548 L 164 598 L 662 598 L 706 551 L 706 507 M 416 731 L 416 -132" />
<glyph unicode="%" glyph-name="percent" horiz-adv-x="869" d="M 126 558 L 126 419 L 173 372 L 321 372 L 372 422 L 372 554 L 324 605 L 176 605 L 126 558 M 838 583 L 176 28.4 M 627 189 L 627 50.4 L 677 3.15 L 822 3.15 L 873 53.6 L 873 189 L 825 236 L 677 236 L 627 189" />
<glyph unicode="&amp;" glyph-name="ampersand" horiz-adv-x="854" d="M 718 268 L 718 56.7 L 671 9.45 L 183 9.45 L 135 56.7 L 135 299 L 224 350 M 696 498 L 696 548 L 643 598 L 224 598 L 170 545 L 170 381 L 869 34.6" />
<glyph unicode="&apos;" glyph-name="quotesingle" horiz-adv-x="186" d="M 129 627 L 129 517" />
<glyph unicode="(" glyph-name="parenleft" horiz-adv-x="224" d="M 227 598 L 186 598 L 132 545 L 132 56.7 L 183 6.3 L 227 6.3" />
<glyph unicode=")" glyph-name="parenright" horiz-adv-x="239" d="M 101 595 L 145 595 L 202 539 L 202 59.9 L 151 9.45 L 104 9.45" />
<glyph unicode="*" glyph-name="asterisk" horiz-adv-x="419" d="M 148 296 L 258 435 L 85 495 M 252 614 L 255 435 L 425 495 M 255 435 L 362 290" />
<glyph unicode="+" glyph-name="plus" horiz-adv-x="381" d="M 249 66.1 L 249 410 M 78.8 239 L 422 239" />
<glyph unicode="," glyph-name="comma" horiz-adv-x="145" d="M 104 22.1 L 104 -126 L 145 -85 L 145 18.9 L 104 22.1" />
<glyph unicode="-" glyph-name="hyphen" horiz-adv-x="454" d="M 97.6 243 L 447 243" />
<glyph unicode="." glyph-name="period" horiz-adv-x="167" d="M 104 22.1 L 104 -12.6 L 151 -12.6 L 151 22.1 L 104 22.1" />
<glyph unicode="/" glyph-name="slash" horiz-adv-x="454" d="M 47.2 31.5 L 510 573" />
<glyph unicode="0" glyph-name="zero" horiz-adv-x="762" d="M 129 536 L 129 59.9 L 186 6.3 L 684 6.3 L 743 63 L 743 548 L 693 598 L 192 598 L 129 536 M 135 63 L 737 551" />
<glyph unicode="1" glyph-name="one" horiz-adv-x="334" d="M 113 444 L 268 624 L 290 624 L 290 -22.1" />
<glyph unicode="2" glyph-name="two" horiz-adv-x="740" d="M 129 504 L 129 542 L 192 605 L 684 605 L 740 545 L 740 353 L 684 296 L 189 296 L 129 236 L 129 9.45 L 765 9.45" />
<glyph unicode="3" glyph-name="three" horiz-adv-x="740" d="M 123 504 L 123 558 L 161 595 L 643 595 L 699 539 L 699 356 L 658 315 L 224 315 L 658 315 L 718 255 L 718 66.1 L 662 9.45 L 170 9.45 L 126 56.7 L 126 81.9" />
<glyph unicode="4" glyph-name="four" horiz-adv-x="652" d="M 558 -22.1 L 558 614 L 63 192 L 696 192" />
<glyph unicode="5" glyph-name="five" horiz-adv-x="759" d="M 145 97.7 L 145 63 L 198 9.45 L 702 9.45 L 759 66.1 L 759 255 L 706 309 L 142 309 L 142 595 L 788 595" />
<glyph unicode="6" glyph-name="six" horiz-adv-x="721" d="M 646 598 L 183 598 L 132 548 L 132 63 L 192 3.15 L 684 3.15 L 740 59.9 L 740 258 L 684 312 L 164 312 L 129 343" />
<glyph unicode="7" glyph-name="seven" horiz-adv-x="598" d="M 47.2 595 L 501 595 L 558 542 L 558 -25.2" />
<glyph unicode="8" glyph-name="eight" horiz-adv-x="740" d="M 195 9.45 L 687 9.45 L 740 63 L 740 261 L 684 318 L 170 318 L 126 362 L 126 545 L 183 602 L 680 602 L 737 545 L 737 362 L 690 312 L 170 312 L 123 268 L 123 59.9 L 195 9.45" />
<glyph unicode="9" glyph-name="nine" horiz-adv-x="740" d="M 142 6.3 L 671 6.3 L 731 63 L 731 545 L 671 605 L 192 605 L 129 539 L 129 350 L 186 293 L 724 293" />
<glyph unicode=":" glyph-name="colon" horiz-adv-x="164" d="M 101 495 L 101 454 L 151 454 L 151 495 L 101 495 M 97.6 22.1 L 97.6 -18.9 L 145 -18.9 L 145 22.1 L 97.6 22.1" />
<glyph unicode=";" glyph-name="semicolon" horiz-adv-x="164" d="M 123 495 L 123 450 L 167 450 L 167 495 L 123 495 M 126 15.8 L 126 -123 L 164 -85 L 164 15.8 L 126 15.8" />
<glyph unicode="&#x3c;" glyph-name="less" horiz-adv-x="397" d="M 406 457 L 59.9 249 L 413 44.1" />
<glyph unicode="=" glyph-name="equal" horiz-adv-x="558" d="M 94.5 334 L 567 334 M 88.2 145 L 570 145" />
<glyph unicode="&#x3e;" glyph-name="greater" horiz-adv-x="416" d="M 94.5 469 L 466 246 L 97.6 37.8" />
<glyph unicode="?" glyph-name="question" horiz-adv-x="598" d="M 81.9 598 L 576 598 L 636 539 L 636 334 L 576 274 L 284 274 L 220 211 L 220 167 M 198 22.1 L 198 -15.8 L 236 -15.8 L 236 18.9 L 198 22.1" />
<glyph unicode="@" glyph-name="at" horiz-adv-x="759" d="M 586 189 L 586 372 L 529 428 L 375 428 L 315 372 L 315 227 L 365 176 L 756 176 L 756 539 L 696 598 L 202 598 L 145 542 L 145 56.7 L 195 6.3 L 753 6.3" />
<glyph unicode="A" glyph-name="A" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1" />
<glyph unicode="B" glyph-name="B" horiz-adv-x="756" d="M 129 595 L 639 595 L 706 529 L 706 372 L 668 315 L 170 315 L 135 350 L 135 284 L 170 315 L 668 315 L 724 261 L 724 59.9 L 668 3.15 L 126 3.15 L 129 595" />
<glyph unicode="C" glyph-name="C" horiz-adv-x="718" d="M 750 602 L 186 602 L 126 542 L 126 63 L 186 3.15 L 753 3.15" />
<glyph unicode="D" glyph-name="D" horiz-adv-x="756" d="M 126 598 L 126 6.3 L 662 6.3 L 721 66.1 L 721 542 L 665 598 L 126 598" />
<glyph unicode="E" glyph-name="E" horiz-adv-x="687" d="M 696 6.3 L 129 6.3 L 129 312 L 583 312 L 129 312 L 129 598 L 693 598" />
<glyph unicode="F" glyph-name="F" horiz-adv-x="627" d="M 126 -22.1 L 126 312 L 586 312 L 126 312 L 126 602 L 693 602" />
<glyph unicode="G" glyph-name="G" horiz-adv-x="756" d="M 532 293 L 718 293 L 718 75.6 L 649 6.3 L 186 6.3 L 126 66.1 L 126 539 L 195 608 L 668 608 L 718 558 L 718 507" />
<glyph unicode="H" glyph-name="H" horiz-adv-x="759" d="M 129 624 L 129 -22.1 L 129 309 L 737 309 L 737 624 L 737 -15.8" />
<glyph unicode="I" glyph-name="I" horiz-adv-x="161" d="M 126 624 L 126 -25.2" />
<glyph unicode="J" glyph-name="J" horiz-adv-x="702" d="M 680 627 L 680 47.2 L 636 3.15 L 129 3.15 L 72.5 63 L 72.5 120" />
<glyph unicode="K" glyph-name="K" horiz-adv-x="702" d="M 126 627 L 126 -18.9 L 126 312 L 406 312 L 674 -15.8 L 403 312 L 677 627" />
<glyph unicode="L" glyph-name="L" horiz-adv-x="706" d="M 148 621 L 148 9.45 L 772 9.45" />
<glyph unicode="M" glyph-name="M" horiz-adv-x="828" d="M 129 -15.8 L 129 617 L 161 614 L 472 249 L 781 617 L 810 617 L 810 -22.1" />
<glyph unicode="N" glyph-name="N" horiz-adv-x="759" d="M 123 -15.8 L 123 611 L 167 611 L 696 -12.6 L 721 -12.6 L 718 617" />
<glyph unicode="O" glyph-name="O" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542" />
<glyph unicode="P" glyph-name="P" horiz-adv-x="706" d="M 123 -22.1 L 123 595 L 674 595 L 721 548 L 721 302 L 671 252 L 170 252 L 123 299" />
<glyph unicode="Q" glyph-name="Q" horiz-adv-x="794" d="M 841 9.45 L 180 9.45 L 126 63 L 126 548 L 180 602 L 665 602 L 724 542 L 724 56.7 L 674 9.45" />
<glyph unicode="R" glyph-name="R" horiz-adv-x="737" d="M 123 -22.1 L 123 598 L 668 598 L 721 545 L 721 312 L 665 258 L 167 258 L 120 306 L 167 258 L 466 258 L 696 -22.1" />
<glyph unicode="S" glyph-name="S" horiz-adv-x="740" d="M 126 97.7 L 126 50.4 L 167 9.45 L 668 9.45 L 715 56.7 L 715 261 L 668 309 L 173 309 L 126 359 L 126 548 L 183 605 L 674 605 L 721 558 L 721 507" />
<glyph unicode="T" glyph-name="T" horiz-adv-x="671" d="M 394 -22.1 L 394 598 L 72.5 598 L 712 598" />
<glyph unicode="U" glyph-name="U" horiz-adv-x="743" d="M 126 621 L 126 59.9 L 176 6.3 L 671 6.3 L 721 59.9 L 721 627" />
<glyph unicode="V" glyph-name="V" horiz-adv-x="917" d="M 123 621 L 498 -18.9 L 882 624" />
<glyph unicode="W" glyph-name="W" horiz-adv-x="1067.8" d="M 117 621 L 353 -15.8 L 589 627 L 844 -25.2 L 1080.4 630" />
<glyph unicode="X" glyph-name="X" horiz-adv-x="721" d="M 142 -15.8 L 687 624 L 416 302 L 142 621 L 690 -22.1" />
<glyph unicode="Y" glyph-name="Y" horiz-adv-x="724" d="M 104 621 L 397 261 L 397 -22.1 L 397 261 L 690 621" />
<glyph unicode="Z" glyph-name="Z" horiz-adv-x="737" d="M 94.5 598 L 718 598 L 718 548 L 135 59.9 L 135 9.45 L 721 9.45" />
<glyph unicode="[" glyph-name="bracketleft" horiz-adv-x="220" d="M 227 6.3 L 129 6.3 L 129 595 L 227 595" />
<glyph unicode="\" glyph-name="backslash" horiz-adv-x="454" d="M 41 598 L 504 34.6" />
<glyph unicode="]" glyph-name="bracketright" horiz-adv-x="233" d="M 94.5 598 L 183 598 L 183 12.6 L 94.5 12.6" />
<glyph unicode="^" glyph-name="asciicircum" horiz-adv-x="564" d="M 608 290 L 334 611 L 63 290" />
<glyph unicode="_" glyph-name="underscore" horiz-adv-x="724" d="M 91.4 -69.3 L 759 -69.3" />
<glyph unicode="`" glyph-name="grave" horiz-adv-x="164" d="M 104 898 L 132 784" />
<glyph unicode="a" glyph-name="a" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236" />
<glyph unicode="b" glyph-name="b" horiz-adv-x="592" d="M 123 677 L 123 9.45 L 545 9.45 L 595 63 L 595 422 L 542 476 L 164 476 L 129 441" />
<glyph unicode="c" glyph-name="c" horiz-adv-x="617" d="M 627 6.3 L 180 6.3 L 126 63 L 126 425 L 180 479 L 627 479" />
<glyph unicode="d" glyph-name="d" horiz-adv-x="595" d="M 580 674 L 580 6.3 L 148 6.3 L 91.4 66.1 L 91.4 416 L 145 469 L 529 469 L 576 425" />
<glyph unicode="e" glyph-name="e" horiz-adv-x="617" d="M 624 3.15 L 176 3.15 L 126 56.7 L 126 422 L 180 479 L 545 479 L 598 425 L 598 243 L 123 243" />
<glyph unicode="f" glyph-name="f" horiz-adv-x="343" d="M 123 -18.9 L 123 472 L 387 472 L 123 472 L 123 602 L 176 655 L 391 655" />
<glyph unicode="g" glyph-name="g" horiz-adv-x="614" d="M 186 -211 L 539 -211 L 595 -154 L 595 428 L 539 485 L 164 485 L 107 428 L 107 50.4 L 154 3.15 L 536 3.15 L 592 59.9" />
<glyph unicode="h" glyph-name="h" horiz-adv-x="602" d="M 126 -18.9 L 126 677 L 126 476 L 545 476 L 602 422 L 602 -22.1" />
<glyph unicode="i" glyph-name="i" horiz-adv-x="145" d="M 126 -22.1 L 123 -15.8 L 123 495 M 107 633 L 107 674 L 148 674 L 148 633 L 107 633" />
<glyph unicode="j" glyph-name="j" horiz-adv-x="202" d="M -126 -214 L 113 -214 L 167 -158 L 167 501 M 145 627 L 145 674 L 189 674 L 189 627 L 145 627" />
<glyph unicode="k" glyph-name="k" horiz-adv-x="573" d="M 126 674 L 126 -25.2 L 126 239 L 334 239 L 567 501 L 334 239 L 570 -22.1" />
<glyph unicode="l" glyph-name="l" horiz-adv-x="233" d="M 120 677 L 120 63 L 176 6.3 L 277 6.3" />
<glyph unicode="m" glyph-name="m" horiz-adv-x="885" d="M 123 -15.8 L 123 472 L 460 472 L 507 428 L 507 -25.2 L 507 428 L 551 472 L 835 472 L 885 422 L 885 -22.1" />
<glyph unicode="n" glyph-name="n" horiz-adv-x="611" d="M 123 -22.1 L 123 466 L 551 466 L 598 419 L 598 -25.2" />
<glyph unicode="o" glyph-name="o" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413" />
<glyph unicode="p" glyph-name="p" horiz-adv-x="586" d="M 129 -243 L 129 469 L 558 469 L 602 428 L 602 40.9 L 561 0 L 180 0 L 135 44.1" />
<glyph unicode="q" glyph-name="q" horiz-adv-x="598" d="M 573 -236 L 573 472 L 139 472 L 88.2 425 L 88.2 59.9 L 142 6.3 L 513 6.3 L 567 56.7" />
<glyph unicode="r" glyph-name="r" horiz-adv-x="438" d="M 126 -25.2 L 126 425 L 180 482 L 498 482" />
<glyph unicode="s" glyph-name="s" horiz-adv-x="617" d="M 126 81.9 L 126 50.4 L 170 6.3 L 548 6.3 L 595 56.7 L 595 192 L 551 236 L 183 236 L 132 287 L 132 428 L 186 479 L 542 479 L 592 428 L 592 400" />
<glyph unicode="t" glyph-name="t" horiz-adv-x="346" d="M 126 680 L 126 472 L 387 472 L 126 472 L 126 50.4 L 161 12.6 L 387 12.6" />
<glyph unicode="u" glyph-name="u" horiz-adv-x="630" d="M 142 498 L 142 53.6 L 186 9.45 L 561 9.45 L 614 66.1 L 614 504" />
<glyph unicode="v" glyph-name="v" horiz-adv-x="706" d="M 110 498 L 397 -22.1 L 699 504" />
<glyph unicode="w" glyph-name="w" horiz-adv-x="973" d="M 120 491 L 324 3.15 L 542 495 L 778 9.45 L 970 501" />
<glyph unicode="x" glyph-name="x" horiz-adv-x="614" d="M 135 -22.1 L 570 498 L 353 239 L 135 501 L 573 -18.9" />
<glyph unicode="y" glyph-name="y" horiz-adv-x="595" d="M 186 -211 L 539 -211 L 595 -154 L 595 501 L 595 40.9 L 558 6.3 L 158 6.3 L 104 59.9 L 104 498" />
<glyph unicode="z" glyph-name="z" horiz-adv-x="633" d="M 104 476 L 608 476 L 608 438 L 110 40.9 L 110 9.45 L 605 9.45" />
<glyph unicode="{" glyph-name="braceleft" horiz-adv-x="239" d="M 246 9.45 L 195 9.45 L 151 53.6 L 151 230 L 75.6 306 L 151 381 L 151 545 L 202 598 L 246 598" />
<glyph unicode="|" glyph-name="bar" horiz-adv-x="161" d="M 123 750 L 123 -129" />
<glyph unicode="}" glyph-name="braceright" horiz-adv-x="239" d="M 107 9.45 L 154 9.45 L 198 53.6 L 198 230 L 277 306 L 202 381 L 202 545 L 148 598 L 107 598" />
<glyph unicode="~" glyph-name="asciitilde" horiz-adv-x="340" d="M 69.3 261 L 158 274 L 293 214 L 365 233" />
<glyph unicode="&#xa0;" glyph-name="nbspace" horiz-adv-x="378" />
<glyph unicode="&#xa1;" glyph-name="exclamdown" horiz-adv-x="173" d="M 132 -12.6 L 132 454 M 151 595 L 151 630 L 113 630 L 117 595 L 151 595" />
<glyph unicode="&#xa2;" glyph-name="cent" horiz-adv-x="161" d="M 627 6.3 L 180 6.3 L 126 63 L 126 425 L 180 479 L 627 479 M 375 750 L 375 -129" />
<glyph unicode="&#xa5;" glyph-name="yen" horiz-adv-x="724" d="M 104 621 L 397 261 L 397 -22.1 L 397 261 L 690 621 M 224 180 L 573 180 M 224 306 L 573 306" />
<glyph unicode="&#xa6;" glyph-name="brokenbar" horiz-adv-x="48.2" d="M 207 225 L 207 -38.7 M 207 697 L 207 434" />
<glyph unicode="&#xa8;" glyph-name="dieresis" horiz-adv-x="567" d=" M 200 684 L 200 649 L 248 649 L 248 684 L 200 684 M 448 684 L 448 649 L 496 649 L 496 684 L 448 684" />
<glyph unicode="&#xa9;" glyph-name="copyright" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 564 458 L 282 458 L 252 428 L 252 189 L 282 159 L 565 159" />
<glyph unicode="&#xaa;" glyph-name="ordfeminine" horiz-adv-x="306" d="M 176 805 L 398 805 L 425 780 L 425 570 L 213 570 L 187 595 L 187 685 L 422 685" />
<glyph unicode="&#xab;" glyph-name="guillemotleft" horiz-adv-x="238" d="M 163 365 L 23.9 199 L 165 35.3 M 289 365 L 150 199 L 291 35.3" />
<glyph unicode="&#xae;" glyph-name="registered" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 250 146 L 250 457 L 523 457 L 550 430 L 550 313 L 521 287 L 272 287 L 249 310 L 272 287 L 422 287 L 537 146" />
<glyph unicode="&#xb0;" glyph-name="degree" horiz-adv-x="265" d="M 161 711 L 161 566 L 177 551 L 324 551 L 339 566 L 339 713 L 324 727 L 176 728 L 161 711" />
<glyph unicode="&#xb1;" glyph-name="plusminus" horiz-adv-x="305" d="M 532 5.04 L 811 5.04 M 653 242 L 653 517 M 517 381 L 791 381" />
<glyph unicode="&#xb2;" glyph-name="twosuperior" horiz-adv-x="370" d="M 191 819 L 191 838 L 222 869 L 468 869 L 496 839 L 496 743 L 468 715 L 220 715 L 191 685 L 191 572 L 509 572" />
<glyph unicode="&#xb3;" glyph-name="threesuperior" horiz-adv-x="370" d="M 187 819 L 187 846 L 206 865 L 447 865 L 476 836 L 476 745 L 455 724 L 238 724 L 455 724 L 485 695 L 485 600 L 457 572 L 211 572 L 189 595 L 189 608" />
<glyph unicode="&#xb4;" glyph-name="acute" horiz-adv-x="378" d=" M 377 757 L 251 586" />
<glyph unicode="&#xb7;" glyph-name="middot" horiz-adv-x="260" d="M 200 329 L 200 287 L 257 287 L 257 329 L 200 329" />
<glyph unicode="&#xb9;" glyph-name="onesuperior" horiz-adv-x="167" d="M 183 789 L 260 879 L 271 879 L 271 556" />
<glyph unicode="&#xba;" glyph-name="ordmasculine" horiz-adv-x="265" d="M 161 711 L 161 566 L 177 551 L 324 551 L 339 566 L 339 713 L 324 727 L 176 728 L 161 711" />
<glyph unicode="&#xbb;" glyph-name="guillemotright" horiz-adv-x="249" d="M 37.8 375 L 186 197 L 39.1 30.2 M 164 375 L 312 197 L 165 30.2" />
<glyph unicode="&#xbc;" glyph-name="onequarter" horiz-adv-x="532" d="M 68 682 L 161 790 L 174 790 L 174 403 M 173 31.5 L 636 573 M 807 -13.2 L 807 369 L 510 115 L 890 115" />
<glyph unicode="&#xbd;" glyph-name="onehalf" horiz-adv-x="580" d="M 68 682 L 161 790 L 174 790 L 174 403 M 173 31.5 L 636 573 M 550 302 L 550 325 L 588 363 L 883 363 L 917 327 L 917 212 L 883 178 L 586 178 L 550 142 L 550 5.67 L 932 5.67" />
<glyph unicode="&#xbe;" glyph-name="threequarters" horiz-adv-x="752" d="M 73.7 718 L 73.7 750 L 96.4 773 L 386 773 L 420 739 L 420 629 L 395 605 L 134 605 L 395 605 L 431 569 L 431 455 L 397 421 L 102 421 L 75.6 450 L 75.6 465 M 173 31.5 L 636 573 M 807 -13.2 L 807 369 L 510 115 L 890 115" />
<glyph unicode="&#xbf;" glyph-name="questiondown" horiz-adv-x="598" d="M 636 -15.8 L 142 -15.8 L 81.9 44.1 L 81.9 249 L 142 309 L 435 309 L 498 372 L 498 416 M 520 561 L 520 598 L 482 598 L 482 564 L 520 561" />
<glyph unicode="&#xc0;" glyph-name="Agrave" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M 296 866 L 394 734" />
<glyph unicode="&#xc1;" glyph-name="Aacute" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M 614 915 L 488 745" />
<glyph unicode="&#xc2;" glyph-name="Acircumflex" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M 586 760 L 421 953 L 259 760" />
<glyph unicode="&#xc3;" glyph-name="Atilde" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M 252 828 L 340 841 L 476 781 L 548 800" />
<glyph unicode="&#xc4;" glyph-name="Adieresis" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M 290 873 L 290 838 L 337 838 L 337 873 L 290 873 M 529 873 L 529 838 L 577 838 L 577 873 L 529 873" />
<glyph unicode="&#xc5;" glyph-name="Aring" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M 353 1013.0 L 353 868 L 369 853 L 517 853 L 532 868 L 532 1015.9 L 517 1029.1 L 369 1030.0 L 353 1013.0" />
<glyph unicode="&#xc8;" glyph-name="Egrave" horiz-adv-x="687" d="M 696 6.3 L 129 6.3 L 129 312 L 583 312 L 129 312 L 129 598 L 693 598 M 271 866 L 369 734" />
<glyph unicode="&#xc9;" glyph-name="Eacute" horiz-adv-x="687" d="M 696 6.3 L 129 6.3 L 129 312 L 583 312 L 129 312 L 129 598 L 693 598 M 581 918 L 455 748" />
<glyph unicode="&#xca;" glyph-name="Ecircumflex" horiz-adv-x="687" d="M 696 6.3 L 129 6.3 L 129 312 L 583 312 L 129 312 L 129 598 L 693 598 M 571 760 L 406 953 L 244 760" />
<glyph unicode="&#xcb;" glyph-name="Edieresis" horiz-adv-x="687" d="M 696 6.3 L 129 6.3 L 129 312 L 583 312 L 129 312 L 129 598 L 693 598 M 262 873 L 262 838 L 309 838 L 309 873 L 262 873 M 507 873 L 507 838 L 554 838 L 554 873 L 507 873" />
<glyph unicode="&#xcc;" glyph-name="Igrave" horiz-adv-x="161" d="M 126 624 L 126 -25.2 M 7.88 866 L 106 734" />
<glyph unicode="&#xcd;" glyph-name="Iacute" horiz-adv-x="161" d="M 126 624 L 126 -25.2 M 321 958 L 195 787" />
<glyph unicode="&#xce;" glyph-name="Icircumflex" horiz-adv-x="161" d="M 126 624 L 126 -25.2 M 300 760 L 135 953 L -27.4 760" />
<glyph unicode="&#xcf;" glyph-name="Idieresis" horiz-adv-x="161" d="M 126 624 L 126 -25.2 M -9.2 873 L -9.2 838 L 38 838 L 38 873 L -9.2 873 M 252 873 L 252 838 L 299 838 L 299 873 L 252 873" />
<glyph unicode="&#xd0;" glyph-name="Eth" horiz-adv-x="756" d="M 66.1 243 L 416 243 M 126 598 L 126 6.3 L 662 6.3 L 721 66.1 L 721 542 L 665 598 L 126 598" />
<glyph unicode="&#xd1;" glyph-name="Ntilde" horiz-adv-x="759" d="M 123 -15.8 L 123 611 L 167 611 L 696 -12.6 L 721 -12.6 L 718 617 M 259 828 L 348 841 L 483 781 L 555 800" />
<glyph unicode="&#xd2;" glyph-name="Ograve" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 296 866 L 394 734" />
<glyph unicode="&#xd3;" glyph-name="Oacute" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 586 916 L 460 746" />
<glyph unicode="&#xd4;" glyph-name="Ocircumflex" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 586 760 L 421 953 L 259 760" />
<glyph unicode="&#xd5;" glyph-name="Otilde" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 252 828 L 340 841 L 476 781 L 548 800" />
<glyph unicode="&#xd6;" glyph-name="Odieresis" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 283 873 L 283 838 L 330 838 L 330 873 L 283 873 M 536 873 L 536 838 L 583 838 L 583 873 L 536 873" />
<glyph unicode="&#xd7;" glyph-name="multiply" horiz-adv-x="614" d="M 135 -22.1 L 570 498 L 353 239 L 135 501 L 573 -18.9" />
<glyph unicode="&#xd8;" glyph-name="Oslash" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M 68 -90.7 L 735 689" />
<glyph unicode="&#xd9;" glyph-name="Ugrave" horiz-adv-x="743" d="M 126 621 L 126 59.9 L 176 6.3 L 671 6.3 L 721 59.9 L 721 627 M 299 866 L 397 734" />
<glyph unicode="&#xda;" glyph-name="Uacute" horiz-adv-x="743" d="M 126 621 L 126 59.9 L 176 6.3 L 671 6.3 L 721 59.9 L 721 627 M 602 960 L 476 790" />
<glyph unicode="&#xdb;" glyph-name="Ucircumflex" horiz-adv-x="743" d="M 126 621 L 126 59.9 L 176 6.3 L 671 6.3 L 721 59.9 L 721 627 M 588 760 L 423 953 L 261 760" />
<glyph unicode="&#xdc;" glyph-name="Udieresis" horiz-adv-x="743" d="M 126 621 L 126 59.9 L 176 6.3 L 671 6.3 L 721 59.9 L 721 627 M 287 873 L 287 838 L 334 838 L 334 873 L 287 873 M 539 873 L 539 838 L 586 838 L 586 873 L 539 873" />
<glyph unicode="&#xdd;" glyph-name="Yacute" horiz-adv-x="724" d="M 104 621 L 397 261 L 397 -22.1 L 397 261 L 690 621 M 605 953 L 479 783" />
<glyph unicode="&#xe0;" glyph-name="agrave" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M 233 740 L 331 608" />
<glyph unicode="&#xe1;" glyph-name="aacute" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M 511 784 L 385 614" />
<glyph unicode="&#xe2;" glyph-name="acircumflex" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M 529 609 L 365 801 L 202 609" />
<glyph unicode="&#xe3;" glyph-name="atilde" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M 210 671 L 298 684 L 434 624 L 506 643" />
<glyph unicode="&#xe4;" glyph-name="adieresis" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M 219 684 L 219 649 L 267 649 L 267 684 L 219 684 M 474 684 L 474 649 L 521 649 L 521 684 L 474 684" />
<glyph unicode="&#xe5;" glyph-name="aring" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M 274 824 L 274 679 L 290 664 L 438 664 L 453 679 L 453 827 L 438 840 L 289 841 L 274 824" />
<glyph unicode="&#xe8;" glyph-name="egrave" horiz-adv-x="617" d="M 624 3.15 L 176 3.15 L 126 56.7 L 126 422 L 180 479 L 545 479 L 598 425 L 598 243 L 123 243 M 236 740 L 334 608" />
<glyph unicode="&#xe9;" glyph-name="eacute" horiz-adv-x="617" d="M 624 3.15 L 176 3.15 L 126 56.7 L 126 422 L 180 479 L 545 479 L 598 425 L 598 243 L 123 243 M 512 811 L 386 641" />
<glyph unicode="&#xea;" glyph-name="ecircumflex" horiz-adv-x="617" d="M 624 3.15 L 176 3.15 L 126 56.7 L 126 422 L 180 479 L 545 479 L 598 425 L 598 243 L 123 243 M 531 609 L 367 801 L 204 609" />
<glyph unicode="&#xeb;" glyph-name="edieresis" horiz-adv-x="617" d="M 624 3.15 L 176 3.15 L 126 56.7 L 126 422 L 180 479 L 545 479 L 598 425 L 598 243 L 123 243 M 226 684 L 226 649 L 273 649 L 273 684 L 226 684 M 473 684 L 473 649 L 520 649 L 520 684 L 473 684" />
<glyph unicode="&#xec;" glyph-name="igrave" horiz-adv-x="145" d="M 126 -22.1 L 123 -15.8 L 123 495  M 0 740 L 97.7 608" />
<glyph unicode="&#xed;" glyph-name="iacute" horiz-adv-x="145" d="M 126 -22.1 L 123 -15.8 L 123 495  M 275 813 L 149 643" />
<glyph unicode="&#xee;" glyph-name="icircumflex" horiz-adv-x="145" d="M 126 -22.1 L 123 -15.8 L 123 495  M 295 609 L 130 801 L -32.1 609" />
<glyph unicode="&#xef;" glyph-name="idieresis" horiz-adv-x="145" d="M 126 -22.1 L 123 -15.8 L 123 495  M -11.8 684 L -11.8 649 L 35.5 649 L 35.5 684 L -11.8 684 M 239 684 L 239 649 L 286 649 L 286 684 L 239 684" />
<glyph unicode="&#xf1;" glyph-name="ntilde" horiz-adv-x="611" d="M 123 -22.1 L 123 466 L 551 466 L 598 419 L 598 -25.2 M 210 671 L 298 684 L 434 624 L 506 643" />
<glyph unicode="&#xf2;" glyph-name="ograve" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M 244 740 L 342 608" />
<glyph unicode="&#xf3;" glyph-name="oacute" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M 505 799 L 379 629" />
<glyph unicode="&#xf4;" glyph-name="ocircumflex" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M 536 609 L 371 801 L 209 609" />
<glyph unicode="&#xf5;" glyph-name="otilde" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M 217 671 L 306 684 L 441 624 L 513 643" />
<glyph unicode="&#xf6;" glyph-name="odieresis" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M 228 684 L 228 649 L 275 649 L 275 684 L 228 684 M 487 684 L 487 649 L 534 649 L 534 684 L 487 684" />
<glyph unicode="&#xf7;" glyph-name="divide" horiz-adv-x="680" d="M 387 479 L 387 444 L 435 444 L 435 479 L 387 479 M 387 195 L 387 161 L 435 161 L 435 195 L 387 195 M 146 337 L 671 337" />
<glyph unicode="&#xf8;" glyph-name="oslash" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M 186 0 L 608 493" />
<glyph unicode="&#xf9;" glyph-name="ugrave" horiz-adv-x="630" d="M 142 498 L 142 53.6 L 186 9.45 L 561 9.45 L 614 66.1 L 614 504 M 243 740 L 340 608" />
<glyph unicode="&#xfa;" glyph-name="uacute" horiz-adv-x="630" d="M 142 498 L 142 53.6 L 186 9.45 L 561 9.45 L 614 66.1 L 614 504 M 519 782 L 393 612" />
<glyph unicode="&#xfb;" glyph-name="ucircumflex" horiz-adv-x="630" d="M 142 498 L 142 53.6 L 186 9.45 L 561 9.45 L 614 66.1 L 614 504 M 535 609 L 370 801 L 208 609" />
<glyph unicode="&#xfc;" glyph-name="udieresis" horiz-adv-x="630" d="M 142 498 L 142 53.6 L 186 9.45 L 561 9.45 L 614 66.1 L 614 504 M 225 684 L 225 649 L 272 649 L 272 684 L 225 684 M 487 684 L 487 649 L 534 649 L 534 684 L 487 684" />
<glyph unicode="&#xfd;" glyph-name="yacute" horiz-adv-x="595" d="M 186 -211 L 539 -211 L 595 -154 L 595 501 L 595 40.9 L 558 6.3 L 158 6.3 L 104 59.9 L 104 498 M 511 799 L 385 629" />
<glyph unicode="&#xff;" glyph-name="ydieresis" horiz-adv-x="595" d="M 186 -211 L 539 -211 L 595 -154 L 595 501 L 595 40.9 L 558 6.3 L 158 6.3 L 104 59.9 L 104 498 M 210 684 L 210 649 L 258 649 L 258 684 L 210 684 M 467 684 L 467 649 L 514 649 L 514 684 L 467 684" />
<glyph unicode="&#x2013;" glyph-name="endash" horiz-adv-x="680" d="M 146 243 L 671 243" />
<glyph unicode="&#x2014;" glyph-name="emdash" horiz-adv-x="907" d="M 195 243 L 895 243" />
<glyph unicode="&#x201c;" glyph-name="quotedblleft" horiz-adv-x="461" d="M 174 666 L 187 564 M 316 666 L 329 564" />
<glyph unicode="&#x201d;" glyph-name="quotedblright" horiz-adv-x="461" d="M 145 666 L 132 564 M 286 666 L 274 564" />
<glyph unicode="&#x2039;" glyph-name="guilsinglleft" horiz-adv-x="159" d="M 163 365 L 23.9 199 L 165 35.3" />
<glyph unicode="&#x203a;" glyph-name="guilsinglright" horiz-adv-x="166" d="M 37.8 375 L 186 197 L 39.1 30.2" />
<glyph unicode="&#x20ac;" glyph-name="Euro" horiz-adv-x="718" d="M 750 602 L 186 602 L 126 542 L 126 63 L 186 3.15 L 753 3.15 M 66.1 180 L 416 180 M 66.1 306 L 416 306" />
<glyph unicode="&#x0178;" glyph-name="Ydieresis" horiz-adv-x="724" d="M 104 621 L 397 261 L 397 -22.1 L 397 261 L 690 621 M 274 873 L 274 838 L 321 838 L 321 873 L 274 873 M 532 873 L 532 838 L 580 838 L 580 873 L 532 873" />
<glyph unicode="&#x102;" glyph-name="Abreve" horiz-adv-x="737" d="M 126 -25.2 L 126 542 L 186 602 L 662 602 L 718 542 L 718 258 L 123 258 L 718 258 L 718 -22.1 M630.484 987.933L630.644 883.713L590.259 849.236L232.099 848.321L188.66 889.025L188.553 987.933" />
<glyph unicode="&#x114;" glyph-name="Ebreve" horiz-adv-x="687" d="M 696 6.3 L 129 6.3 L 129 312 L 583 312 L 129 312 L 129 598 L 693 598 M614.484 987.933L614.644 883.713L574.259 849.236L216.099 848.321L172.66 889.025L172.553 987.933" />
<glyph unicode="&#x11E;" glyph-name="Gbreve" horiz-adv-x="756" d="M 532 293 L 718 293 L 718 75.6 L 649 6.3 L 186 6.3 L 126 66.1 L 126 539 L 195 608 L 668 608 L 718 558 L 718 507 M636.484 987.933L636.644 883.713L596.259 849.236L238.099 848.321L194.66 889.025L194.553 987.933" />
<glyph unicode="&#x12C;" glyph-name="Ibreve" horiz-adv-x="161" d="M 126 624 L 126 -25.2 M407.484 987.933L407.644 883.713L367.259 849.236L9.09936 848.321L-34.3403 889.025L-34.447 987.933" />
<glyph unicode="&#x14E;" glyph-name="Obreve" horiz-adv-x="737" d="M 126 542 L 126 59.9 L 180 9.45 L 671 9.45 L 721 59.9 L 721 551 L 671 595 L 176 598 L 126 542 M630.484 987.933L630.644 883.713L590.259 849.236L232.099 848.321L188.66 889.025L188.553 987.933" />
<glyph unicode="&#x16C;" glyph-name="Ubreve" horiz-adv-x="743" d="M 126 621 L 126 59.9 L 176 6.3 L 671 6.3 L 721 59.9 L 721 627 M632.484 987.933L632.644 883.713L592.259 849.236L234.099 848.321L190.66 889.025L190.553 987.933" />
<glyph unicode="&#x103;" glyph-name="abreve" horiz-adv-x="611" d="M 101 476 L 545 476 L 598 425 L 598 6.3 L 173 6.3 L 123 56.7 L 123 236 L 592 236 M590.484 847.933L590.644 743.713L550.259 709.236L192.099 708.321L148.66 749.025L148.553 847.933" />
<glyph unicode="&#x115;" glyph-name="ebreve" horiz-adv-x="617" d="M 624 3.15 L 176 3.15 L 126 56.7 L 126 422 L 180 479 L 545 479 L 598 425 L 598 243 L 123 243 M592.484 847.933L592.644 743.713L552.259 709.236L194.099 708.321L150.66 749.025L150.553 847.933" />
<glyph unicode="&#x11F;" glyph-name="gbreve" horiz-adv-x="614" d="M 186 -211 L 539 -211 L 595 -154 L 595 428 L 539 485 L 164 485 L 107 428 L 107 50.4 L 154 3.15 L 536 3.15 L 592 59.9 M591.484 847.933L591.644 743.713L551.259 709.236L193.099 708.321L149.66 749.025L149.553 847.933" />
<glyph unicode="&#x12D;" glyph-name="ibreve" horiz-adv-x="145" d="M 126 -22.1 L 123 -15.8 L 123 495  M442.484 847.933L442.644 743.713L402.259 709.236L44.0994 708.321L0.65975 749.025L0.55297 847.933" />
<glyph unicode="&#x14F;" glyph-name="obreve" horiz-adv-x="633" d="M 145 413 L 145 63 L 198 6.3 L 564 6.3 L 614 56.7 L 614 435 L 570 482 L 208 482 L 145 413 M597.484 847.933L597.644 743.713L557.259 709.236L199.099 708.321L155.66 749.025L155.553 847.933" />
<glyph unicode="&#x16D;" glyph-name="ubreve" horiz-adv-x="630" d="M 142 498 L 142 53.6 L 186 9.45 L 561 9.45 L 614 66.1 L 614 504 M596.484 847.933L596.644 743.713L556.259 709.236L198.099 708.321L154.66 749.025L154.553 847.933" />
<glyph unicode="&#x2D8;" glyph-name="breve" horiz-adv-x="564" d="M556.484 427.933L556.644 323.713L516.259 289.236L158.099 288.321L114.66 329.025L114.553 427.933" />
<glyph unicode="&#xC6;" glyph-name="AE" horiz-adv-x="1380.0" d="M180 -14.4414L180 543.029C178.903 589.804 191.373 601.955 240 602L778 602M772 263.901L177 263.901M1342 4.30005L775 4.30005L775 310L1229 310L775 310L775 600.035L1339 600.035" />
<glyph unicode="&#x15E;" glyph-name="Scedilla" horiz-adv-x="740" d="M432.993 9.43262L432.993 -110.27L342.788 -110.27M126 97.7L126 50.4L167 9.45L668 9.45L715 56.7L715 261L668 309L173 309L126 359L126 548L183 605L674 605L721 558L721 507" />
<glyph unicode="&#xc7;" glyph-name="Ccedilla" horiz-adv-x="718" d="M474.113 2.91259L474.113 -116.79L383.908 -116.79M750 602L186 602L126 542L126 63L186 3.15L753 3.15" />
<glyph unicode="&#x131;" glyph-name="dotlessi" horiz-adv-x="145" d="M126 -22.1L123 -15.8L123 495" />
<glyph unicode="&#xe7;" glyph-name="ccedilla" horiz-adv-x="617" d="M386.732 5.89907L386.732 -91.9867L312.99 -91.9867M627 6.3L180 6.3L126 63L126 425L180 479L627 479" />
<glyph unicode="&#x15F;" glyph-name="scedilla" horiz-adv-x="617" d="M368.975 6.69454L368.975 -94.9412L292.385 -94.9412M126 81.9L126 50.4L170 6.3L548 6.3L595 56.7L595 192L551 236L183 236L132 287L132 428L186 479L542 479L592 428L592 400" />
<glyph unicode="&#xb8;" glyph-name="cedilla" horiz-adv-x="718" d="M474.113 2.91259L474.113 -116.79L383.908 -116.79" />
<glyph unicode="&#xE6;" glyph-name="ae" horiz-adv-x="1120.0" d="M101 476L545 476L598 425L598 2.3L177 2.3L123 56.7L123 240.135L595.325 240.534L1070.69 240.932L1070.69 425L1017.69 476.932L552.694 476.932L651.269 476.306L598.694 422L598.694 56.7L598.694 3.15L1096.69 3.15" />
<glyph unicode="&#x130;" glyph-name="Idotaccent" horiz-adv-x="161" d="M98.1441 749.5L98.1441 790.5L139.144 790.5L139.144 749.5L98.1441 749.5M126 624L126 -25.2" />
<glyph unicode="&#xa3;" glyph-name="sterling" horiz-adv-x="706" d="M500.059 575.354L458.613 615.217L189.798 615.217L149.144 575.354L148 9.45L732 9.45M66.1 253L416 253" />
<glyph unicode="&#xdf;" glyph-name="germandbls" horiz-adv-x="756" d="M129 595L639 595L706 529L706 372L668 315L270 315L668 315L724 261L724 59.9L668 3.15L270 3.15M126 3.15L129 595" />
"""
FOOTER = """
</font>
</defs>
</svg>"""



def get_missing_glyph():
    d = "M 0,0 0,800 800,800 800,0 0,0 M 0,0 800,800 M 200,0 800,600 M 400,0 800,400 M 0,200 600,800"
    text = f'<missing-glyph horiz-adv-x="{X_ADVANCE}" d="{d}"/> \n'
    return text


def myround(x, base=5):
    return base * round(x/base)

def convert_string_strokes(strokes,round_base=None):
    running_string = ''
    for stroke in strokes:
        current_stroke = ''
        for i, substroke in enumerate(stroke):
            if round_base:
                substroke[0],substroke[1] = myround(substroke[0],base=round_base),myround(substroke[1],base=round_base)
            if i == 0:
                current_stroke += f'M {substroke[0]} {substroke[1]} '
            else:
                current_stroke += f'L {substroke[0]} {substroke[1]} '
        running_string += current_stroke
    return running_string


def convert_full_entry(row):
    return f'<glyph unicode="{row.character}" glyph-name="{row.character}" horiz-adv-x="{X_ADVANCE}" d="{row.combined_lines}" /> \n'


def create_font(font_name,round_base=None):
    df = pd.read_json('graphics.txt', lines=True)
    df['combined_lines'] = df.medians.apply(lambda x :convert_string_strokes(x,round_base=round_base))
    df['full_entries'] = df.apply(lambda x: convert_full_entry(x), axis=1)

    with open(font_name, 'w') as f:
        f.write(HEADER)
        f.write(get_missing_glyph())
        f.write(ENGLISH_CHARECTERS)
        for entry in df['full_entries'].values:
            f.write(entry)
        f.write(FOOTER)



if __name__ == '__main__':
    create_font('danxianziti.svg')
