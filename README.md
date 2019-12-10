# czai4art

This repo contains the code associated with my submission to the Duke AI for Art competition. The code I used to generate the output is included in `tester.ipynb`

Here's the final output. Row 1 and row 4 contain art images fed to the model. Row 2, 3, 5, and 6 contain generated flowery images painted by the model. The model is capable of taking a single abstract painting and generate multiple renditions of flowers using the diversity-sensitive cycleGAN model we created for a class project.

DS-cycleGAN is a novel architecture that improves upon published works such as [cycleGAN](https://arxiv.org/abs/1703.10593) and [DS-CGAN](https://arxiv.org/abs/1901.09024). It combines the advantages of both models, and it's capable of tackling the challenging multimodal unpaired image-to-image translation task. Visit [here](https://github.com/chriszhou0916/DS-cycleGAN) for more information about the architecture used to generate the art.

![combined](images/output/combined.png)

### Inspiration
Abstract art elicits a mélange of emotions from the common museum-goer: intrigue, apathy, or often, confusion. “_I_ can paint that,” they say. “My _child_ can do that.” But to me, abstract art’s abstruse nature liberates the viewer by stripping away prescribed meaning – it challenges the viewer to fuse their own experiences, thoughts, and feelings into the work, essentially walking away with an interpretation that they and the artist have co-created. In this project, “I challenge the AI to “interpret” a set of abstract art, by training it with what society traditionally views as beauty: flowers. “The Virtual Garden” shows that with a little imagination (and in this case, lots of images), you can find your _own_ beauty in almost anything.

### Caption
Images in row 1 in "The Virtual Garden" are selected art pieces found on fineartamerica.com. I created a model that transforms paintings in row 1 into AI generated flowers. The model **stochastically** adds its own coloring and interpretation to generate **unique images** every time the code is executed, hence the different outputs in rows 2 and 3. No two executions will produce the same art piece. Rows 4, 5, 6 and created similarly. Row 4 are art pieces from fineartamerica.com; rows 5 and 6 are generated images resembling flowers.

In "The Virtual Garden", AI doesn't exactly follow human instructions to create art deterministically. Instead, it exercises its own bit of imagination and creativity to create its own diverse garden.
