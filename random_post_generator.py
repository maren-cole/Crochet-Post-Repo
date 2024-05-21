from flask import Flask, jsonify
import random

app = Flask(__name__)


crochet_patterns = [
    {
        "name": "Mini Dino",
        "description": "A miniature colorful dino pattern for beginners.",
        "level": "beginner",
        "time": "2 hours",
        "tools": ["3 mm crochet hook", "8 ply (DK) cotton in the color of your\
                   choice", "8 ply (DK) cotton in blue",
                  "Black embroidery thread to embroider mouth", "Pink\
                      embroidery thread to embroider cheek",
                  "yarn needle", "Polyester fibrefill stuffing", "8mm safety\
                      eyes"],
        "size": "7.5cm Tall",
        "tutorial": {"Head and Body": ["R1: 6 dc in magic circle [6 sts]",
                                       "R2: (inc) x 6 [12 sts]",
                                       "R3: (dc 1, inc) x 6 [18 sts]",
                                       "R4: (dc 1, inc, dc 1) x 6 [24 sts]",
                                       "R5: (dc 3, inc) x 6 [30 sts]",
                                       "R6: dc in each st [30 sts]",
                                       "R7: (dc 7, inc, dc 7) x 2 [32 sts]",
                                       "R8: (dc 15, inc) x 2 [34 sts]",
                                       "R9: (dc 8, inc, dc 8) x 2 [36 sts]",
                                       "R10: dc in each st [36 sts]",
                                       "R11: (dc 5, inc) x 6 [42 sts]",
                                       "R12 - R15: dc in each st i.e. 4 rounds\
                                         [42 sts]",
                                       "Place safety eyes between rounds 9 and\
                                          10 (st 12 and st 18). This placing\
                                          is important as we will be\
                                             crocheting the tail to the body.",
                                       "Embroider a mouth between the eyes and\
                                          some cheeks next to the eyes.",
                                       "R16: dc 34, ch 8, skip 8 sts [42 sts]",
                                       "We will be crocheting the tail using\
                                          this chain and the skipped 8\
                                              stitches later on",
                                       "R17 - R18: dc in each st i.e. 2 rounds\
                                          [42 sts]",
                                       "R19: (dc 5, dec) x 6 [36 sts]",
                                       "R20: (dc 2, dec, dc 2) x 6 [30 sts]",
                                       "R21: (dc 3, dec) x 6 [24 sts]",
                                       "R22: (dc 1, dec, dc 1) x 6 [18 sts]",
                                       "Begin stuffing",
                                       "R23: (dec) x 9 [9 sts]",
                                       "Finish stuffing",
                                       "Fasten off and leave a long thread.\
                                          Thread the yarn through the front\
                                              loops of the 9 sts and pull to\
                                                  close. Weave in the end."
                                       ],
                     "Tail": ["Re-join yarn to first skipped stitch of R16\
                               using a standing dc (or your preferred method).\
                               The standing dc will count as the first st of\
                               the round. Note: refer to video links on page 3\
                               which show how to re-join yarn using a standing\
                               dc as well as how to crochet the tail into the\
                             skipped stitches and chain from R16 of the body",
                              "R1: dc in each st [16 sts]",
                              "R2: (dc 3, dec, dc 3) x 2 [14 sts]",
                              "R3: (dc 5, dec) x 2 [12 sts]",
                              "R4: (dc 2, dec, dc 2) x 2 [10 sts]",
                              "Begin stuffing",
                              "R5: (dc 3, dec) x 2 [8 sts]",
                              "R6: (dc 1, dec, dc 1) x 2 [6 sts]",
                              "R7: (dc 1, dec) x 2 [4 sts]",
                              "Finish stuffing",
                              "Fasten off and leave a long thread. Thread the\
                                  yarn through the front loops of the 4 sts\
                                      and pull to close. Weave in the end."
                              ],
                     "Small Spike (1)": ["8 ply cotton in blue",
                                         "R1: 4 dc in magic circle [4 sts]",
                                         "R2: (dc 1, inc) x 2 [6 sts]",
                                         "R3: (dc 1, inc, dc 1) x 2 [8 sts]",
                                         "Fasten off and leave a long thread\
                                            for sewing - we will be using\
                                            the thread from the small spike\
                                             to sew all the spikes to the body"
                                         ],
                     "Medium Spike (3)": ["R1: 4 dc in magic circle [4 sts]",
                                          "R2: (dc 1, inc) x 2 [6 sts]",
                                          "R3: (dc 1, inc, dc 1) x 2 [8 sts]",
                                          "R4: (dc 3, inc) x 2 [10 sts]",
                                          "Fasten off - no need to leave a\
                                             long thread as we will be using\
                                             the thread from the small spike\
                                             to sew these spikes to the body"
                                          ],
                     "Put it Together": ["Sew small spike over rounds 1 and 3\
                                          of the head and body",
                                         "Sew the 3 medium spikes in a line\
                                         using the thread from small spike"
                                         ]},
    },
    {
     "name": "Crochet Hearts",
     "description": "A crochet hearts pattern for spreading love and joy.",
     "level": "beginner",
     "time": "1 hour",
     "tools": ["yarn", "3.5mm crochet hook"],
     "size": "4 in. wide",
     "instructions": [
        "Chain 4.",
        "Do the following in the first chain you made: 3 treble crochet, 3\
             double crochet, 1 treble crochet, 3 double crochet, 3 treble\
                  crochet, chain 2, 1 slip stitch.",
        "Chain 3.",
        "Do 3 single crochet in the first treble crochet of the previous row.",
        "Do 3 single crochet in the 2nd treble crochet of the previous row.",
        "Do 1 single crochet in each of the next four stitches.",
        "In the treble crochet that’s actually the bottom/point of the hearts:\
              1 single crochet, 1 double crochet, 1 single crochet.",
        "Do 1 single crochet in each of the next four stitches.",
        "Do 3 single crochet in the next treble crochet of the previous row.",
        "Do 3 single crochet in the next (last) treble crochet of the previous\
         row.",
        "Chain 3. Do 1 slip stitch in the middle. Fasten off."
     ]},
    {
     "name": "Chunky Mesh Overshirt",
     "description": "This chunky overshirt is worked sleeve to sleeve. First,\
        one sleeve is worked, then chains are added to either side of the\
        sleeve to create the foundation rows for the back and front body\
        panels. While working the body panels, the front panel is separated\
         to create the cardigan-style opening. Finally, the 2nd sleeve is\
         worked. The piece is folded in half, seamed along the underarms and\
         sides, and a simple, single crochet collar is added.",
     "level": "Intermediate",
     "time": "15 hours",
     "tools": ["300-400 yards (275-360m) of super bulky cotton yarn",
               "10mm hook"],
     "size": ["S/M 36in (90cm), L/XL 42in (105cm), 2X/3X 52in (135cm)"],
     "instructions": {
        "pattern": [
            "To begin, chain 30 (34, 38)",
            "Row 1: Skip the first chain, and work 1sc in each remaining\
             chain. 29 (33, 37) sts.",
            "Row 2: Ch1, turn, 1sc in each st.",
            "Row 3: Ch4 (counts as 1dc and ch1) skip the next st, make\
             1dc in the next st. *Ch1 skip the next st, make 1dc in the\
             next st* repeat between ** to the end of the row.",
            "Repeat row 3 for a total of 5 rows of mesh."
        ],
        "first_sleeve": [
            "With working yarn still attached to your project, chain 29",
            "Panel row 1: Skip the first 5 chs (counts as 1dc, ch1 and skipped\
             ch) work 1dc into the 6th chain. *Ch1, skip 1ch, 1dc in next ch*\
             repeat between ** until you reach your sleeve. Ch1, 1dc in the\
             dc on the sleeve and continue working in the dc mesh pattern\
             across the sleeve."
        ],
        "back_panel": [
            "Repeat instructions for front panel. When you work across the new\
             back panel chains and across the sleeve, continue working in the\
             mesh pattern across the front panel stitches as well."
        ],
        "growing_panels": [
            "Continue working in the dc mesh pattern until your front panel\
             has 7 (9, 11) rows and your back panel has 6 (8, 10) rows."
        ],
        "pattern_continued": [
            "On the next row: Continue working in the dc mesh until you've\
             completed a total of 23 (24, 25) dc sts. Then, ch 39 (41, 43).",
            "Again, skip the first 5 chs and work 1dc in the 6th chain and\
             continue working in the dc mesh along your entire piece until\
             your 2nd front panel has 6 (8, 10) rows."
        ],
        "front_panel_opening": [
            "On the 7 (9, 10)th front panel row, work only the first 28\
             (30, 32) dcs. Ch4, turn and work back the other way for 15\
             (17, 19) dcs (counting your turning chain). Ch4, turn and\
             continue working in dc mesh for 5 sleeve rows. Finish off\
             with 2 rows of single crochet."
        ],
        "other_sleeve": [
            "Fold your piece in half and seam along the underside of the\
             sleeves and along the sides of the body panels. I added an\
             optional row of single crochet all along the front edge of\
             my shirt. Work 1sc for each chain and dc, for an even edge."
        ],
        "collar": [
            "Fasten on a new yarn along the neck opening, 13 dc stitches\
             up from the bottom edge of one of the front panels. Work in\
             single crochet up around the neck to the stitch 13 dcs up from\
             the bottom of the other front panel. Work 6 rows of sc total,\
             fasten off."
        ]}
    },
    {
     "name": "Cleo the Clam",
     "description": "Meet Cleo! When you live your entire life in a shell, you\
     can tend to be a little shy... But Cleo is determined to move past this\
     clam stereotype and meet new friends. He keeps his clam shell propped\
     open as often as he can, and greets any passersby with a cheery “hello!”",
     "level": "beginner",
     "time": "2 hours",
     "tools": [
         "Crochet hook size: 3.75mm",
         "Medium/worsted weight yarn: tan (outer shell) and cream\
              (inner shell)",
         "Light/light worsted: peach (clam)",
         "Yarn needle",
         "One pair of 12 mm safety eyes",
         "Polyester fiber fill stuffing",
         "One strand of black embroidery floss for the mouth and eyebrows"
     ],
     "size": "Final measurement for the finished shell will be 3 inches\
          (7.5 cm) wide and the little clam inside will be 1.25 inches\
              (3.25 cm) tall.",
     "instructions": {
        "pattern": [
            "Outer Shell",
            "With tan yarn,",
            "Round 1: Ch 2, 6 sc in first ch. (6 sts)",
            "R2: 2 sc in each st around. (12 sts)",
            "R3: (Sc 1, 2 sc in next st), 6 times. (18 sts)",
            "R4: (Sc 2, 2 sc in next st), 6 times. (24 sts)",
            "R5: (Sc 3, 2 sc in next st), 6 times. (30 sts)",
            "R6: (Sc 4, 2 sc in next st), 6 times. (36 sts)",
            "R7: (Sc 17, 2 sc in next st), 2 times. (38 sts)",
            "R8: Sc 38. (38 sts)",
            "Wait to fasten off until you have made the inner shell pieces.\
             (Also wait to crochet the 2nd outer shell until you have made\
             both inner shells.)"
        ],
        "inner_shell": [
            "Inner Shell (make 2)",
            "With cream yarn,",
            "R1: Ch 2, 6 sc in first ch. (6 sts)",
            "R2: 2 sc in each st around. (12 sts)",
            "R3: (Sc 1, 2 sc in next st), 6 times. (18 sts)",
            "R4: (Sc 2, 2 sc in next st), 6 times. (24 sts)",
            "R5: (Sc 3, 2 sc in next st), 6 times. (30 sts)",
            "R6: (Sc 4, 2 sc in next st), 6 times. (36 sts)",
            "R7: (Sc 17, 2 sc in next st), 2 times. (38 sts)",
            "Fasten off, leaving a yarn tail for weaving in. You will now be\
             crocheting the shell pieces together.",
            "Insert your crochet hook back into the outer shell right where\
             you left off at the end of R8. Then insert your hook through a\
             stitch of the outer shell and a stitch of the inner shell, as\
             pictured to the right. Single crochet all the way around the 2\
             shell pieces to join them. Fasten off, leaving a yarn tail for\
             sewing."
        ],
        "clam_option_1": [
            "The Clam Option 1 - with light/light worsted yarn",
            "With peach yarn,",
            "R1: Ch 2, 6 sc in first ch. (6 sts)",
            "R2: 2 sc in each st around. (12 sts)",
            "R3: (Sc 3, 2 sc in next st), 3 times. (15 sts)",
            "R4: (Sc 4, 2 sc in next st), 3 times. (18 sts)",
            "R5: (Sc 5, 2 sc in next st), 3 times. (21 sts)",
            "R6-7: Sc 21. (2 total rounds)",
            "R8: (Sc 6, 2 sc in next st), 3 times. (24 sts)",
            "R9: Sc 24. (24 sts)",
            "R10: (Sc 2, dec 1), 6 times. (18 sts)",
            "R11: (Sc 1, dec 1), 6 times. (12 sts)",
            "R12: Dec 6 times. (6 sts)",
            "Fasten off, leaving a yarn tail for sewing. Jump to “Finish\
             stuffing…” below to finish making your clam."
        ],
        "clam_option_2": [
            "The Clam Option 2 - with medium/medium worsted yarn",
            "With peach yarn,",
            "R1: Ch 2, 6 sc in first ch. (6 sts)",
            "R2: 2 sc in each st around. (12 sts)",
            "R3: (Sc 3, 2 sc in next st), 3 times. (15 sts)",
            "R4: (Sc 4, 2 sc in next st), 3 times. (18 sts)",
            "R5-7: Sc 18. (3 total rounds)",
            "R8: (Sc 1, dec 1), 6 times. (12 sts)",
            "R9: Dec 6 times. (6 sts)",
            "Fasten off, leaving a yarn tail for sewing."
        ],
        "finish_clam": [
            "Finish stuffing the body as needed you want the body to hold\
             its shape but still be squishy.",
            "Use the yarn tail and your yarn needle to weave through the 6 sts\
             around the opening and pull tight to close, as pictured to the\
             right. Secure with a knot and weave in your end.",
            "Place the clam inside his shell, and… you are finished! Thank yo\
             so much for joining me in making a cute little clam!"
        ]}
    },
    {
     "name": "Simplest Twist Headband",
     "description": "This pattern by Doraly Crochet is perfect for beginners,\
         offering a quick and easy project to start building your crochet\
         collection. It's a one-piece, uncomplicated pattern that is\
         adjustable with simple instructions. The headband features a charming\
         twist detail, making it a stylish accessory for any outfit.",
     "level": "beginner",
     "time": "",
     "tools": [
         "Yarn - A size 3 DK weight yarn",
         "4mm (US G-6) crochet hook or appropriate hook for your yarn",
         "Tapestry needle",
         "Scissors"
     ],
     "size": "Yardage will vary according to the thickness of the yarn chosen\
          for the headband. The pattern's samples used approximately 42 meters\
         (46 yards). The headband is adjustable by increasing or decreasing\
         the number of chains to fit comfortably around your head.",
     "instructions": [
        "1. Begin by chaining 106 stitches. Test the length around your head\
         to ensure it's comfortable, adjusting the number of chains as\
         needed.",
        "2. Row 1: Chain 2, then half double crochet (hdc) in every chain.",
        "3. Rows 2 to 6: Chain 2 and turn, then hdc in every stitch. Adjust\
         the thickness of the headband by adding or removing rows.",
        "4. To finish, chain 1 and cut the yarn, leaving a 20cm (8) tail for\
         sewing. Pull on the tail to tightly fasten the chain.",
        "5. The Twist: Thread the tail into a tapestry needle. Ensure there is\
         no twisting in the body of the headband, then bring the two ends\
         together, placing them like two Cs facing each other, interlocked.\
         Pass the needle through the extension of the two ends, capturing all\
         4 layers. Sew back and forth as needed to tightly secure the ends.",
        "6. If desired, knot the tail and hide it by running it through a few\
         stitches on the underside of the headband. Cut the remaining yarn.\
         Repeat the process with the starting tail.",
        "7. Turn the sewn seam inside out to expose the twist, tweaking it\
         open if needed.",
        "8. Your Simplest Twist Headband is now ready to wear and show off!"]
    },
    {
     "name": "Positive Potato",
     "description": "Designed by Leanna Booth, August 2023. These Positive\
     Potatoes are very popular with children. This simple design is quick and\
     easy to make, measuring 7cm (2.75”). They make adorable gifts or\
     additions to backpacks, bringing smiles wherever they go.",
     "level": "beginner",
     "time": "",
     "tools": [
        "20g 8ply(DK) yarn in beige or any potato-colored yarn",
        "Black yarn for embroidering mouth",
        "Size 3.5mm (UK 9, US 4) crochet hook",
        "Stuffing",
        "2 x 8mm safety eyes (or embroider if for a child under 3)",
        "A small clip or clasp for attaching to backpacks (optional)"
     ],
     "size": "Approximately 7cm (2.75”) tall",
     "instructions": [
        "1. With a 3.5mm hook and 8ply yarn, make 6 double crochet (dc) into\
         a magic circle.",
        "2. 2dc in each stitch around (12 stitches). Place marker and move\
         after every round.",
        "3. (Dc, 2dc) around (18 stitches).",
        "4-8. Dc around for 5 rounds.",
        "5. Place eyes between rows 5 and 6 with 3 stitches in between.",
        "9. (Dc 5, 2dc) around (21 stitches).",
        "10. Dc around.",
        "11. (Dc 6, 2dc) around (24 stitches).",
        "12. Dc around.",
        "13. (Dc 6, dc decrease) around (21 stitches).",
        "14. (Dc 5, dc decrease) around (18 stitches).",
        "15. (Dc, dc decrease) around (12 stitches). Stuff potato.",
        "16. (Dc decrease) around (6 stitches). Top up stuffing, cut yarn, and\
         thread through the last 6 stitches. Pull up tight, finish off (FO).",
        "Arms/hand (make 2):",
        "1. Leaving a long end, chain 3, turn.",
        "2. Double crochet (dc) in 2nd chain from hook, dc (2), turn.",
        "3-4. Chain 1, dc 2.",
        "5. Double crochet decrease (dc dec), FO leaving a long end of yarn.",
        "Print the sheet of sayings. Cut out your chosen saying leaving a\
         margin on each side. Place a piece of sticky tape across the saying\
         to strengthen it.",
        "Centre the saying on the body of the potato, placing the arms on each\
         side so that the hands are on the margin of the saying. Pin the arms\
         in place and stitch firmly across the ends.",
        "Using the long end of yarn at the hand end, and holding the saying in\
         place, push the needle through the saying in the middle of the\
         margin. Secure the end firmly by weaving through the body.",
        "Make a mouth using black yarn.",
        "Attach a clasp or keyring chain (optional)."]
    },
    {
     "name": "Crochet Fruit Coasters Pattern",
     "description": "Create adorable fruit-themed coasters with this free\
     pattern by Annemarie Benthem. Perfect for adding a pop of color to your\
     table setting or as a fun gift for friends and family. The pattern\
     includes instructions for making an apple, lemon, and orange coaster.",
     "level": "beginner",
     "time": "1 hour",
     "tools": [
        "Paintbox Cotton Aran yarn in various colors (Granite Grey,\
         Lime Green, Tomato Red, Blood Orange, Buttercup Yellow)",
        "Crochet hook size 4mm (US G-6)",
        "Scissors",
        "Sewing needle"
     ],
     "size": "Approximately 10cm (4”) in diameter",
     "instructions": {
        "fruit": [
            "Start with the following color: Apple: use Tomato Red, Lemon: use\
             Buttercup Yellow, Orange: use Blood Orange",
            "1. Chain 4. Attach the first to the last with a slip stitch\
             (SLST). You can also start with a magic ring. If you don't know\
             how to make a magic ring, click here.",
            "2. Chain 2, 10 double crochet (DC) in the ring. Attach the \
            first to the last with a SLST. (10)",
            "3. Chain 2, 2DC in every DC of the previous row. Attach the\
             first to the last with a SLST. (20)",
            "4. Chain 2, 2DC in every DC of the previous row. Attach the first\
             to the last with a SLST. (40)",
            "5. 40 single crochet (SC). (40)"
        ],
        "stem": [
            "Stem (with Granite Grey):",
            "1. Chain 8.",
            "2. 1SC in the 2nd stitch.",
            "3. 6SLST in the next 6 stitches. Finish off."
        ],
        "leaf": [
            "Leaf (with Lime Green):",
            "1. Chain 6.",
            "2. 1SC in the 2nd stitch. In the next stitches: 1 half double\
             crochet (HDC), 1DC, 1HDC, 1SC.",
            "3. In the same stitch as the last SC of the previous row: 1SC.\
             Now continue on the other side of the 6 chains of the first row:\
             1HDC, 1DC, 1HDC, 1SC. Make 1SLST in the next stitch, which is the\
             first SC you made at the beginning of row 2.",
            "4. Now SLST through the middle of the leaf back down to the\
             beginning of the leaf to get a stripe in the middle of the leaf."
        ],
        "assembly": [
            "After making the stem and the leaf: sew them onto the fruit.\
             Fasten off and work away all yarn ends."
        ]}
    },
    {
     "name": "Flower Hexagon Bag Pattern",
     "description": "Create a beautiful flower hexagon bag with this pattern\
     by Adorably Kawaii. Perfect for using up leftover scrap yarns and adding\
     a touch of charm to your accessories. The bag features flower hexagons\
     joined together and topped with straps for easy carrying.",
     "level": "intermediate",
     "time": "",
     "tools": [
        "Worsted weight yarn in three colors (main color, contrasting color,\
         second contrasting color)",
        "Crochet hook size E/3.5mm",
        "Scissors",
        "Tapestry needle"
     ],
     "size": "Hexagons are about 3”(7.6cm) across between the points and each\
     straight side is about 1.5” (3.8cm). The bag is 10”(25cm) wide \
     and 9”(22.8cm) tall, excluding the straps.",
     "instructions": {
        "tips": [
            "Crochet over yarn ends as you go along to minimize weaving in\
             ends later."
        ],
        "flower_hexagon": [
            "Flower Hexagon (Make 21):",
            "With contrasting color yarn,",
            "R1: 5 single crochet (sc) into magic ring. Cut yarn. Join the end\
             of the round with invisible join. (6 sts. The invisible join\
             counts as a st.)",
            "With main color yarn,",
            "R2: Pull up a loose loop in a st and work 4 hdc puff st in the\
             same st. Chain 2. *5 hdc puff stitch in next st, ch 2* repeat 5\
             times. Join the end of the round with a slip stitch.\
             (6 puff st petals) Cut yarn. Pull the yarn end through the\
             last st to the back of the work.",
            "With second contrasting color yarn,",
            "R3: Insert hook into a ch 2 space and pull up a loop and chain 2\
             (this counts as the first double crochet). *2 double crochet,\
             chain 2, 3 double crochet* into the same space.\
             *3 double crochet, chain 2, 3 double crochet* into the next chain\
             2 space and repeat 4 times more. Cut yarn and leave a tail for\
             sewing. Join the end of the round with invisible join."
        ],
        "assembly": [
            "Assembly:",
            "Arrange your hexagons and join them by single crocheting them\
             together through the back loops only with the right sides facing\
             each other. Then fold and sew up the sides."
        ],
        "top_border": [
            "Top Border:",
            "With main color and the right side of bag facing, insert hook\
             into the top of the bag, chain 2 (counts as first double crochet)\
            , and then double crochet all around. When you get to the points,\
             work 2 double crochet into the chain 2 space."
        ],
        "straps": [
            "Straps (Make 2):",
            "Count 6 stitches in the center of the top hexagon. With main\
             color, chain 2 in the 6th st (counts as first double crochet)\
             and double crochet in the next 5 sts. Chain 2, turn. \
            (6 double crochet) Work in rows until the strap is 15”/38cm long\
             or desired length. Then single crochet the strap onto the other\
             hexagon of the same side with the right sides facing each other.\
             Do the same for the back to make the second strap."
        ]}
    },
    {
     "name": "Arctic Fox Crochet Pattern",
     "description": "Create your own adorable arctic fox with this crochet\
     pattern. This pattern includes instructions for the head, body, snout,\
     ears, front legs, back legs, tail, and scarf. Perfect for crochet\
     enthusiasts!",
     "level": "advanced",
     "time": "",
     "tools": [
        "3 mm Ricorumi hook",
        "Rico embroidery needle",
        "Rico stitch markers"
     ],
     "size": "13 cm, 5 in",
     "instructions": {
        "body": [
            "In patina, working into magic ring, 6 dc.",
            "Work in a spiral in continuous rnds.",
            "Rnd 1: [2 dc into next st] 6 times. 12 sts.",
            "Rnd 2: [2 dc into next st] 12 times. 24 sts.",
            "Rnd 3: [3 dc, 2 dc into next st] 6 times. 30 sts.",
            "Rnd 4: [4 dc, 2 dc into next st] 6 times. 36 sts.",
            "Rnd 5: 17 dc, 2 dc into next st, 17 dc, 2 dc into last st.\
                 38 sts.",
            "Rnds 6 12: 38 dc.",
            "Rnd 13: 17 dc, dc2tog, 17 dc, dc2tog. 36 sts.",
            "Rnd 14: 36 dc.",
            "Rnd 15: [4 dc, dc2tog] 6 times. 30 sts.",
            "Rnd 16: 30 dc.",
            "Rnd 17: [3 dc, dc2tog] 6 times. 24 sts.",
            "Rnd 18: 24 dc.",
            "Rnd 19: [2 dc, dc2tog] 6 times. 18 sts.",
            "Rnd 20: 18 dc.",
            "Fasten off and break yarn, leaving a long tail.",
            "Fill Body with stuffing."
        ],
        "head": [
            "In white attach yarn to last st of Body.",
            "Rnd 1: [2 dc into next st] 18 times. 36 sts.",
            "Rnd 2: [5 dc, 2 dc into next st] 6 times. 42 sts.",
            "Rnd 3: [6 dc, 2 dc into next st] 6 times. 48 sts.",
            "Rnds 4 9: 48 dc. Change yarn.",
            "Rnd 10: In patina [6 dc, dc2tog] 6 times. 42 sts.",
            "Rnds 11 13: 42 dc.",
            "Rnd 14: [5 dc, dc2tog] 6 times. 36 sts",
            "Rnds 15 16: 36 dc.",
            "Rnd 17: [4 dc, dc2tog] 6 times. 30 sts",
            "Rnd 18: [3 dc, dc2tog] 6 times. 24 sts",
            "Rnd 19: [2 dc, dc2tog] 6 times. 18 sts",
            "Rnd 20: [1 dc, dc2tog] 6 times. 12 sts",
            "Fill Head firmly with stuffing.",
            "Rnd 21: [Dc2tog] 6 times. 6 sts.",
            "Fasten off and break yarn, leaving a long tail."
        ],
        "snout": [
            "In white, working into magic ring, 6 dc.",
            "Work in a spiral in continuous rnds.",
            "Rnd 1: [1 dc, 2 dc into next st] 3 times. 9 sts.",
            "Rnd 2: 9 sts.",
            "Rnd 3: [2 dc, 2 dc into next st] 3 times. 12 sts.",
            "Fasten off and break yarn, leaving a long tail."
        ],
        "ears": [
            "EARS (MAKE 2 IN WHITE AND 2 IN PATINA)",
            "Ch2, turn.",
            "Row 1: 2 dc into 2nd ch from hook, turn. 2 dc.",
            "Row 2: 1 ch, [2 dc into next st] 2 times, turn. 4 dc.",
            "Row 3: 1 ch, 2 dc into first st, 2 dc, 2 dc into last st, turn.\
                6 dc.",
            "Row 4: 1 ch, 2 dc into first st, 4 dc, 2 dc into last st, turn.\
                8 dc.",
            "Row 5: 1 ch, 8 dc, turn.",
            "For Ear parts in white fasten off and break yarn.",
            "For Ear parts in patina do not break yarn.",
            "Place 1 Ear part in white and in patina ws together, using patina\
            close seam, work round outside of Ear as follows.",
            "1 ch, 7 dc, [1 dc, 1 ch, 1 dc] all in next st at corner, 5 dc,\
            [1 htr, 1 tr, 1 htr] all in next st at tip of Ear, 5 dc, 1 sl st.",
            "Fasten off and break yarn, leaving a long tail."
        ],
        "front_leg": [
            "FRONT LEG (MAKE 2)",
            "In mouse grey working into magic ring, 6 dc.",
            "Work in a spiral in continuous rnds.",
            "Rnd 1: [1 dc, 2 dc into next st] 3 times. 9 sts.",
            "Rnd 2: [2 dc, 2 dc into next st] 3 times. 12 sts.",
            "Rnds 3 4: 12 dc.",
            "Rnd 5: [2 dc, dc2tog] 3 times. 9 sts.",
            "Rnds 6 7: 9 dc. Change yarn.",
            "Rnds 8 12: In patina 9 dc.",
            "Fill Leg with stuffing. Lay flat and close opening with 4 dc\
             through both layers.",
            "Fasten off and break yarn, leaving a long tail."
        ],
        "back_leg": [
            "BACK LEG (MAKE 2)",
            "THIGH",
            "In patina working into magic ring, 6 dc.",
            "Work in a spiral in continuous rnds.",
            "Rnd 1: [2 dc into next st] 6 times. 12 sts.",
            "Rnd 2: [2 dc into next st] 12 times. 24 sts.",
            "Rnd 3: [3 dc, 2 dc into next st] 6 times. 30 sts.",
            "Fasten off and break yarn, leaving a long tail.",
            "PAW",
            "In mouse grey working into magic ring, 6 dc.",
            "Work in a spiral in continuous rnds.",
            "Rnd 1:",
            "Fill Paw with stuffing. Lay flat and close opening with 4 dc\
             through both layers.",
            "Fasten off and break yarn, leaving a long tail."
        ],
        "tail": [
            "TAIL",
            "In white working into magic ring, 6 dc. Work in a spiral in\
             continuous rnds.",
            "Rnd 1: [1 dc, 2 dc into next st] 6 times. 9 sts.",
            "Rnd 2: 9 dc.",
            "Rnd 3: [2 dc, 2 dc into next st] 3 times. 12 sts.",
            "Rnd 4: [5 dc, 2 dc into next st] 2 times. 14 sts.",
            "Rnd 5: [6 dc, 2 dc into next st] 3 times. 16 sts.",
            "Rnd 6: [3 dc, 2 dc into next st] 4 times. 20 sts.",
            "Rnd 7: [4 dc, 2 dc into next st] 4 times. 24 sts.",
            "Rnd 8: [3 dc, 2 dc into next st] 6 times. 30 sts.",
            "Change yarn.",
            "Rnds 9 11: In patina, 30 dc.",
            "Rnd 12: [3 dc, dc2tog,] 6 times. 24 sts.",
            "Rnds 13 14: 24 dc.",
            "Rnd 15: [2 dc, dc2tog] 6 times. 18 sts.",
            "Rnds 16 17: 18 dc.",
            "Rnd 18: [1 dc, dc2tog] 6 times. 12 sts.",
            "Rnds 19 20: 12 dc.",
            "Fill Tail with stuffing. Lay flat and close opening with 6 dc\
             through both layers.",
            "Fasten off and break yarn, leaving a long tail."
        ],
        "scarf": [
            "SCARF",
            "Ch7 + 1 t-ch, turn.",
            "Row 1: 1 dc into 2nd ch from hook, 6 dc, turn. 7 dc.",
            "Rows 2 37: 1 ch, 7 dc, turn.",
            "Fasten off and break yarn.",
            "Sew both ends of scarf together to make a loop."
        ],
        "to_make_up": [
            "TO MAKE UP",
            "Use long tails to attach pieces to each other.",
            "Fill Snout with stuffing, embroider nose with embroidery thread\
             as illustrated and attach to Head.",
            "Attach Front Legs to Body, between rnds 14 15, 2 sts apart.",
            "Fill Back Legs lightly with stuffing and sew to sides of Body as\
             illustrated.",
            "Lightly fill Thighs with stuffing and attach to sides of Body.",
            "Attach Paws to Body at a slight angle between rnds 3 5 as\
             illustrated.",
            "Attach Tail to back of Body, bend upwards and sideways and attach\
             tip of Tail to one side of Body.",
            "Sew Ears to Head."
        ]}
    },
    {
     "name": "Bermuda Tote Crochet Pattern",
     "description": "Create your own stylish Bermuda Tote with this crochet\
     pattern. This pattern includes instructions for making 13 individual\
     squares, outer edging, and straps. Perfect for a day at the beach or a\
     casual outing!",
     "level": "intermediate",
     "time": "",
     "tools": [
        "US G/6 (4mm) crochet hook",
        "Removable stitch marker",
        "Tapestry needle"
     ],
     "size": "Finished Dimensions: A Length: 15”/38cm B Width: 15”/38cm\
     C Strap Length: 16”/41cm",
     "instructions": {
        "notes": [
            "NOTES:",
            "Bag is made of 13 individual squares which are sewn together to\
             form the shape. Strap is crocheted onto bag after construction.\
             Squares are worked flat in back and forth rows turn at the end\
             of each row. To change color, work the final yarn over of the\
             last stitch in the previous row with the new color. The ch 3 at\
             the beginning of each row counts as a stitch work the first dc\
             of each row in the 2nd stitch, and work the last dc of each row\
             in the top of the turning ch from the row below."
        ],
        "squares": [
            "SQUARES (MAKE 13):",
            "With color A, ch 4.",
            "Row 1: In 4th ch from hook, dc 1, tr 1, dc 2. (4 dc + 1 tr)",
            "Row 2: Ch 3, dc 1, (dc 2, tr 1, dc 2) in tr, dc 2. (8 dc + 1 tr)",
            "Place a removable stitch marker on the corner tr st to easily\
             identify it, and move it up each row.",
            "Row 3: Ch 3, dc to tr, (dc 2, tr 1, dc 2) in tr, dc to end of\
             row. (12 dc + 1 tr)",
            "Change to color B.",
            "Rows 4+5: Rep row 3. (20 dc + 1 tr)",
            "Change to color C.",
            "Rows 6+7: Rep row 3. (28 dc + 1 tr)",
            "Change to color D.",
            "Rows 8+9: Rep row 3. (36 dc + 1 tr)",
            "Change to color E.",
            "Rows 10+11: Rep row 3. (44 dc + 1 tr)",
            "Do not fasten off. Rotate work to begin working down the side\
             edge.",
            "Square Border:",
            "Note: When working into the sides of dc rows, insert the hook\
             under two bars of the side of the stitch rather than working\
             around the whole post to prevent large holes.",
            "Ch 1, sc 2 in the side of each dc row to the next corner (22 dc),\
             sc 2 in the corner, rotate work to begin working down next side,\
             sc 2 in the side of each dc row to the next corner (22 dc), sc 2\
             in the corner, rotate work to begin working down next side and\
             starting in the top of the st just worked into, sc in each dc\
             along edge to next corner (22 dc), sc 2 in corner tr, rotate\
             work to begin working down final side, sc in each dc along edge\
             to next corner (22 dc), sc 2 in the corner, sl st to 1st sc to\
             join. (96 sc)",
            "Fasten off. Secure and weave in all ends."
        ],
        "construction": [
            "CONSTRUCTION:",
            "Block all squares to 5.5”/14cm to ensure a perfect fit. Using a\
             whip stitch or seaming technique of your choice, seam the squares\
             together in the configuration illustrated below. Fold squares 12\
             and 13 up to meet squares 1 and 2. Square 8 will be folded in\
             half horizontally. Using the colors and letters on \
             configuration as a guide, seam side A to side B, side C to side\
             D, side E to side F, and so on. Squares 3 and 5 will be folded in\
             half vertically. Secure and weave in all ends."
        ],
        "outer_edging_and_straps": [
            "OUTER EDGING AND STRAPS:",
            "With color A and front of bag (squares 1, 2, 4, 6, 7) facing up,\
             rejoin yarn in the 1st of the 22 sc along the right side edge of\
             square 2 (leave the remaining corner st next to square\
             5 unworked).",
            "Round 1: Ch 1 and starting in same st as join, sc 23 up the right\
             side edge of square 2 (last sc should be in the 1st of the 2\
             corner sts at the top of square 2), ch 68 for front strap, then\
             starting in the 2nd corner st at the top of square 1, sc 23 down\
             the left side edge of square 1 (there should be 1 corner st\
             remaining), sc2tog around the remaining corner sts of squares 1\
             and 12, sc 23 up the right side edge of square 12 (last sc should\
             be in the 1st of the 2 corner sts at the top of square 12), ch 68\
             for back strap, then starting in the 2nd corner st at the top of\
             square 13, sc 23 down the left side edge of square 13 (there\
             should be 1 corner st remaining), sc2tog around the remaining\
             corner sts of squares 13 and 2. Do not join.",
            "Round 2: Sc around, working a sc2tog at the left side corner and\
             again at the end of the round. Fasten off. With front of bag\
             facing up, rejoin yarn in the remaining corner st at the top\
             of square 2.",
            "Round 3: Ch 1 and starting in the same st as join, sc 23 down the\
             left side edge of square 2 (there should be 1 corner st\
             remaining), sc2tog around the remaining corner sts of squares\
             2 and 1, sc 23 up the right side edge of square 1, then sc into\
             the underside of each ch that formed the strap. Do not join.",
            "Round 4: Sc around, working a sc2tog at the center corner. Fasten\
             off. Rep rounds 3 and 4 on back of bag along squares 12 and \
             and opposite strap. Secure and weave in any remaining ends."
        ]}
    },
    {
     "name": "Sunflower Earrings Crochet Pattern",
     "description": "Create charming sunflower earrings with this crochet\
     pattern. The earrings feature a mid-section in brown or black or natural\
     color and yellow petals. They work up quickly and are perfect for adding\
     a touch of sunshine to your outfit!",
     "level": "beginner",
     "time": "",
     "tools": [
        "1.25mm Crochet hook",
        "Tapestry needle and scissors",
        "Stitch marker",
        "Aunt Lydia’s cotton crochet thread no 10 colours \
         and (brown/black or natural )."
     ],
     "size": "Approximately 4cm x 4cm (with a 1.25mm hook)",
     "instructions": [
        "Technical Notes and Gauge:",
        "- This pattern is written using U.S terminology",
        "- Crochet in continuous spiral rounds, unless specified otherwise.\
         Use a stitch marker or piece of yarn to keep track of the last\
         stitch in each round.",
        "- Gauge is not important for this project however by using a 1.25mm\
         hook my earring measured 4cm x 4cm",
        "- You will first work on the mid-section in brown or black or natural\
         of the sunflower then the petals in yellow",
        "- If you are working with the black crochet thread, ensure that you\
         crochet in a well lit area and use a stitch marker.",
        "Mid Section of Sunflower:",
        "Row 1: Make a slip knot, Ch 6, sl st in the first Ch to form a ring.\
         You will work in this ring in row 3.",
        "Note: Mark the first Sc in row 2",
        "Row 2: Ch 1, make 2sc in each St, remove stitch marker, sl st in that\
         St",
        "Note: Mark first Dc in the ring",
        "Row 3: Ch 1, Make 14 Dc in the ring, remove stitch marker - sl st in\
         that St, FO.",
        "Petals:",
        "Note: You will now be working in one stitch at a time which means all\
         of step one must be done in one stitch except the picot stitch",
        "The Picot stitch (P) is done by Ch 2 - sl st in first chain",
        "Step 1: Attach yellow yarn, Ch 4, Tr, P, Tr, Ch 4, sl st.",
        "Step 2: sl st in the next St, Ch 4, Tr, Picot stitch, Tr, Ch 4,\
         sl st.",
        "Steps 3-14: Repeat Row 2 in all the remaining Sts. Fasten off after\
         the 14th petal. Weave in your ends and create another. Now you\
         have a pair.",
        "Attach earring hooks to any one of the picot stitch on each\
         sunflower.\
         Your earring is ready."]
    },
    {
     "name": "Lemon Granny Square Crochet Pattern",
     "description": "Create a delightful lemon granny square with this crochet\
     pattern. The square features a lemon center, bright yellow border, and\
     pistachio outer rounds, adorned with a leaf and surface crochet details.\
     Use it in various projects like blankets, cushions, scarves, or table\
     decorations.",
     "level": "beginner",
     "time": "",
     "tools": [
        "1 ball of paintbox yarns simply DK buttercup yellow",
        "1 ball of budget yarns DK Lemon",
        "1 ball of budget yarns DK pistachio",
        "Small amount of stylecraft special DK Kelly green or dark green\
         alternative",
        "4mm (G-6) Crochet hook",
        "Scissors",
        "Tapestry Needle"
     ],
     "size": "Approximately 13cm x 13cm",
     "instructions": [
        "Pattern begins in lemon yarn",
        "1. In MR Ch 2 (counts as a stitch), 8Htr into the ring. Pull the ring\
         closed and join to the top of the Ch 2 with a sl st. (9)",
        "2. Ch 2 (counts as a st), 1Htr in the base of the Ch 2, 2Htr in each\
         st around, join to the top of the Ch 2 with a sl st. (18)",
        "3. Ch 2 (counts as a st), 1Htr in the st at the base of the Ch 2,\
         1Htr in next st. *2Htr in next st, 1Htr* repeat from * to * around,\
         join with sl st to the top of the beginning Ch 2. (27)",
        "4. Ch 2 (counts as a st), 1Htr in st at the base of the Ch 2, 1Htr in\
         next 2 stitches. *2Htr, 1Htr, 1Htr* repeat from * to * around.\
         Join with a sl st to the top of the beginning Ch 2. (36)",
        "5. Ch 2 (counts as a st), 1Htr in st at the base of the Ch 2, 1Htr in\
         next 3 stitches. *2Htr in next st, 1Htr, 1Htr, 1Htr* repeat from\
         * to * around, join with sl st into the top of the beginning\
         Ch 2. FO (45)",
        "6. Join bright yellow into any stitch on the circle. Ch 1 (does not\
         count as a st) Dc in the same st and Dc in each st around, sl st to\
         Ch1. (45)",
        "7. Ch 1 (does not count as a st) 1Dc in each stitch around in FLO.\
         Join to Ch 1, FO. (45)",
        "8. Join pistachio to BL of any stitch on the Lemon circle from round\
         6 (not the last round worked but the round prior to this you will\
         have back loops exposed. Ch 1 (does not count as a st), 1Dc in same\
         space as Ch 1, 1Dc, *1Htr, 2Tr, Ch 2, 2Tr, 1Htr, 5Dc*. Repeat from\
         * to * twice more. 1Htr, 2Tr, Ch2, 2Tr, 1Htr, 3Dc, sk last st, join\
         to the first Dc. (4 ch 2 spaces and 44 stitches made).",
        "9. Ch 2 (counts as a st), 1 Htr in each st to the corner Ch2 space\
         [2Tr, Ch2, 2Tr] in corner space, repeat around the square, 1Htr in\
         each stitch and [2Tr, Ch2, 2Tr] in corner space. Join to top of\
         beginning Ch2 with a sl st. (4 Ch2 spaces and 60 stitches)",
        "10. Ch 3 (counts as a st), 1Tr in each st to the corner Ch 2 space,\
         [2Tr, Ch2, 2Tr] in corner space. Repeat around, 1Tr in each stitch\
         and [2Tr, Ch2, 2Tr] in each corner, join to top of beginning Ch3 with\
         sl st, FO and weave in ends. (4 Ch2 spaces and 76 stitches).",
        "To make the leaf: Ch 7, 1Htr in second Ch from hook, 4Tr, [1Tr, 1Dc,\
         3Ch picot, 1Dc] into the last Ch stitch. Working down the other side\
         of the chain, 5Tr, 1Htr into the last ch, sl st into the first Htr.\
         FO. Sew leaf into place on the square.",
        "Surface Crochet: Surface crochet a circle on top of the lemon circle\
         with white using the pictures for reference. Surface crochet across\
         the circle horizontally, vertically, and twice diagonally to create\
         the segments.",
        "Weave in your ends and your square is complete!"]
    },
    {
     "name": "EZ Checked Blanket",
     "description": "Create a cozy checked blanket. This pattern features a\
     unique knit-like texture achieved with simple loops and basic joining\
     techniques. The blanket measures approximately 52\" x 52\" and is\
     perfect for adding warmth and style to any room.",
     "level": "intermediate",
     "time": "",
     "tools": [
        "Bernat® Alize® Blanket-EZ™ (6.4 oz/180 g; 18 yds/16 m)",
        "Size U.S. X/X (X mm) crochet hook or size needed to obtain gauge",
        "6 large safety pins"
     ],
     "size": "Approximately 52\" x 52\"",
     "instructions": {
        "strip_one": [
            "Strip One:",
            "1. With MC, count 11 loops for foundation row, noting yarn end is\
             at far right and all loops are facing upwards.",
            "2. 1st row: Working from left to right, pull the 12th loop\
             (from ‘working yarn’) up through 11th loop (last loop of\
             foundation row) from behind to create a knit stitch. Pull next\
             loop from working yarn up through next loop of foundation.\
             Continue in this manner to end of row. Do not turn work. 11\
             stitches in row.",
            "3. 2nd row: Working from right to left, pull next loop from\
             working yarn up from behind through last stitch worked on\
             previous row. *Pull next loop from working yarn up from behind\
             through next stitch. Repeat from * across to end of row. Do not\
             turn.",
            "4. 3rd row: Working from left to right, pull next loop from\
             working yarn up from behind through last stitch worked on\
             previous row. *Pull next loop from working yarn up from behind\
             through next stitch. Repeat from * across to end of row. Do not\
             turn.",
            "5. 4th row: As 2nd row. Repeat 3rd and 4th rows twice more, for a\
             total of 8 rows worked. Cut thread at base of next loop (thread\
             used to create the loop) to create a yarn ‘tail’. You will now\
             join A. Cut thread at base of first loop of A to create a yarn\
             “tail\". Tie tails of MC and A together, and weave in ends.\
             Continue with A, working as given for first 8 rows."
        ],
        "strip_two": [
            "Strip Two:",
            "1. With A, count 11 loops for foundation row, noting yarn end is\
             at far right and all loops are facing upwards.",
            "2. 1st row: Working from left to right, pull the 12th loop\
             (from ‘working yarn’) up through 11th loop (last loop \
             foundation row) from behind to create a knit stitch. Pull next\
             loop from working yarn up through next loop of foundation.\
             Continue in this manner to last loop of foundation row.\
             Place last loop of foundation row over far left loop of first row\
             of Strip One; pull next loop from working yarn up through both\
             loops. Do not turn work. 11 stitches in row.",
            "3. 2nd row: Working from right to left, pull next loop from\
             working yarn up from behind through first loop of second row of\
             Strip One and last stitch worked on previous row. *Pull next loop\
             from working yarn up from behind through next stitch. Repeat from\
             * across to end of row. Do not turn.",
            "4. 3rd row: Working from left to right, pull next loop from\
             working yarn up from behind through last stitch worked on\
             previous row. *Pull next loop from working yarn up from behind\
             through next stitch. Repeat from * to last loop. Pull next loop\
             of working yarn up from behind through first loop of third row of\
             Strip One and last loop of previous row. Do not turn. Continue in\
             this manner, joining work in an ascending manner up left edge of\
             Strip One, until 8 rows have been worked. Cut thread at base of\
             next loop (thread used to create the loop) to create a yarn\
             ‘tail’. You will now join B. Cut thread at base of first loop of\
             B to create a yarn “tail\". Tie tails of A and B together, and\
             weave in ends. Continue with B, working as given for first\
             8 rows."
        ],
        "continue_strips_three_to_six": [
            "Continue in this manner, working 8 rows with A and 8 rows with B,\
             until a total of 56 rows have been worked. Do not bind off. Leave\
             stitches on safety pin to secure. Strips Three to Six: Following\
             the color layout shown in Diagram on page 3, continue working as\
             established for Strips Three to Six, joining sides of Strips as\
             before and leaving stitches for each Strip on safety pin to\
             secure."
        ],
        "strip_seven": [
            "Strip Seven:",
            "With MC, count 10 loops for foundation row, noting yarn end is at\
             far right and all loops are facing upwards.",
            "1st row: Working from left to right, pull the 11th loop (from\
             ‘working yarn’) up through 10th loop (last loop of\
             foundation row) from behind to create a knit stitch. Pull next\
             loop from working yarn up through next loop of foundation.\
             Continue in this manner to last loop of foundation row. Place\
             last loop of foundation row over far left loop of first row of\
             Strip Six; pull next loop from working yarn up through both\
             loops.\
             Do not turn work. 10 stitches in row.",
            "2nd row: Working from right to left, pull next loop from working\
             yarn up from behind through first loop of second row of Strip Six\
             and last stitch worked on previous row. *Pull next loop from\
             working yarn up from behind through next stitch. Repeat from\
             * across to end of row. Do not turn.",
            "3rd row: Working from left to right, pull next loop from working\
             yarn up from behind through last stitch worked on previous row.\
             *Pull next loop from working yarn up from behind through next\
             stitch. Repeat from * to last loop. Pull next loop of working\
             yarn up from behind through first loop of third row of Strip Six\
             and last loop of previous row. Do not turn. Continue in this\
             manner, joining work in an ascending manner up left edge of Strip\
             Six, until 8 rows have been worked.",
            "Bind off row: Working in same direction as last row, across all\
             stitches from safety pins from all Strips, pull 2nd stitch\
             through first stitch. Pull 3rd stitch through 2nd stitch. Pull\
             4th stitch through 3rd stitch. Continue in this manner to end of\
             row. Cut last loop to create yarn ‘tail’. Tie to secure and weave\
             in ends."
        ]}
    },
    {
     "name": "Bumble Blossom Black-Eyed Susan",
     "description": "Craft a delightful Bumble Blossom Black-Eyed Susan,\
     complete with its pot and a cheerful bumblebee. This special flower will\
     never wilt or fade, adding a touch of cheer all year round. With\
     Schachenmayr Catania yarn in various colors and a 2mm crochet hook, you\
     can create this charming project. The finished project measures\
     approximately 12.5cm tall by 10cm wide.",
     "level": "intermediate",
     "time": "",
     "tools": [
        "Schachenmayr Catania yarn in Sonne (00208 yellow), Apfel\
         (00205 green), Teddy (00161 light-brown), Marone (00157 brown), Weiss\
         (00106 white), Schwarz (00110 black)",
        "2mm crochet hook",
        "Sewing needle",
        "Stitch marker",
        "Stuffing material",
        "Cardboard for the pot",
        "Wire for the stem"
     ],
     "size": "Approximately 12.5cm tall by 10cm wide",
     "instructions": {
        "stem": [
            "STEM (MAKE 1):",
            "1. Using green yarn, rnd 1: 8 sc in mr (8), rnd 2-30: 8 sc (8)\
             (29 rounds)",
            "2. Add stuffing material to the stem as you go along.",
            "3. Add wire to the stem for added stability. Measure and cut a\
             piece of wire the length of the stem. Insert the wire into the\
            stem from the opening at the top of the stem and carefully guide\
             the wire through the length of the stem.",
            "4. rnd 31: BLO (1 sc, 1 inc) x 4 (12)",
            "5. rnd 32: 12 inc (24)",
            "6. rnd 33: (3 sc, 1 inc) x 6 (30)",
            "7. Cut the yarn and fasten off, leaving a long tail for sewing.",
            "8. rnd 34: 30 sc (30)",
            "9. Add the sepals to the stem. Holding the stem facing upward,\
             insert the hook into the last remaining loop of round 31 of the\
             stem. Attach green yarn.",
            "10. Ch 9. Starting in the 2nd chain from the hook, 8 sc, slst\
             into the next loop. Repeat 7 more times for a total of 8 sepals.\
             Cut the yarn and fasten off invisibly."
        ],
        "flower_center": [
            "FLOWER CENTER (MAKE 1):",
            "1. Using black yarn, rnd 1: 6 sc in mr (6)",
            "2. rnd 2: 6 inc (12)",
            "3. rnd 3: 12 sc (12)",
            "4. rnd 4: (1 sc, 1 inc) x 6 (18)",
            "5. rnd 5: 18 sc (18)",
            "6. rnd 6: (2 sc, 1 inc) x 6 (24)",
            "7. rnd 7: 24 sc (24)",
            "8. rnd 8: (3 sc, 1 inc) x 6 (30)",
            "9. rnd 9: 30 sc (30)",
            "10. Cut the yarn and fasten off, leaving a long tail for sewing."
        ],
        "petals": [
            "PETALS (MAKE 7):",
            "1. Using yellow yarn, rnd 1: 6 sc in mr (6)",
            "2. rnd 2: 6 inc (12)",
            "3. rnd 3: (1 sc, 1 inc) x 6 (18)",
            "4. rnd 4-7: 18 sc (18) (4 rounds)",
            "5. rnd 8: (4 sc, 1 dec) x 3 (15)",
            "6. rnd 9-12: 15 sc (15) (4 rounds)",
            "7. rnd 13: (3 sc, 1 dec) x 3 (12)",
            "8. rnd 14-17: 12 sc (12) (4 rounds)",
            "9. rnd 18: (2 sc, 1 dec) x 3 (9)",
            "10. Cut the yarn and fasten off, leaving a long tail for sewing."
        ],
        "leaves": [
            "LEAVES (MAKE 2):",
            "1. Using green yarn, rnd 1: 6 sc in mr (6)",
            "2. rnd 2: 5 sc, 1 inc (7)",
            "3. rnd 3: (2 sc, 1 inc) x 2, 1 sc (9)",
            "4. rnd 4: (2 sc, 1 inc) x 3 (12)",
            "5. rnd 5: (3 sc, 1 inc) x 3 (15)",
            "6. rnd 6: (4 sc, 1 inc) x 3 (18)",
            "7. rnd 7-16: 18 sc (18) (10 rounds)",
            "8. rnd 17: (1 sc, 1 dec) x 6 (12)",
            "9. rnd 18: 6 dec (6)",
            "10. Cut the yarn and fasten off, leaving a long tail for sewing."
        ]}
    }
]


@app.route('/random-pattern', methods=['GET'])
def get_random_pattern():
    pattern = random.choice(crochet_patterns)
    return jsonify(pattern)


if __name__ == '__main__':
    app.run()
