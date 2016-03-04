## Delphin XML

This document outlines the format for XML in Delphin, and how to add it to a build of the app in XCode. After reading this document, you will understand the way the Delphin uses XML, and therefore the way to create and add new XML to future versions of Delphin.

#### Layout.xml
Specifies the main font for Delphin, and the specific font sizes of different types of text, on different devices. The set of font sizes for a device is structured as follows:

```xml
<device>
    <model>iPad</model>
    <fontsizes>
        <tappable>24</tappable>
        <regular>24</regular>
        <summary>22</summary>
        <note>16</note>
        <regulartapped>24</regulartapped>
        <summarytapped>22</summarytapped>
        <notetapped>16</notetapped>
        <lemmata>18</lemmata>
        <title>28</title>
        <linenumber>24</linenumber>
    </fontsizes>
</device>
```
The `<model />` tag must match the string that is returned by the Library function .... .

#### Authors.xml
Specifies the authors of all texts in Delphin. For each author listed in this file, there *must exist* a corresponding 'author'.xml file, as the app looks for a file with each author's name. For example, if 'caesar' is listed as an author, Delphin will search for a 'caesar.xml' file. If this file does not exist, the author's texts will not show up in the app (and the app will probably crash).

The authors XML file is structured as follows:

```xml
<authors>
	<author>vergil</author>
	<author>caesar</author>
</authors>
```

#### *[author]*.xml
E.g., 'caesar.xml' (see Authors.xml description above). The easiest way to explain this file structure is to begin with the structure:

```xml
<author>
    <bio>
        <shortName>Caesar</shortName>
        <longName>Gaius Julius Caesar</longName>
        <life>100 - 44 BC</life>
    </bio>
    
    <works>
        <work>
            <title>De Bello Gallico</title>
            <genre>Prose</genre>
            
            <books>
                <book>
                    <title>Liber Primus</title>
                    <heading>Argumentum</heading>
                    <introduction>Lorem ipsum dolor sit amet</introduction>
                    
                    <chapters>
                        <chapter>debellogallico-1.1</chapter>
                        <chapter>debellogallico-1.2</chapter>
                        <chapter>debellogallico-1.3</chapter>
                    </chapters>
                </book>
                <book>
                    <title>Liber Quartus</title>
                    <heading>Argumentum</heading>
                    <introduction>Lorem ipsum dolor sit amet</introduction>
                    
                    <chapters>
                        <chapter>debellogallico-4.24</chapter>
                        <chapter>debellogallico-4.25</chapter>
                        <chapter>debellogallico-4.26</chapter>
                    </chapters>
                </book>
            </books>
        </work>
    </works>
</author>
```

*nb. parts of the file have been cut to keep this concise.*

The structure should be fairly self-explanatory. For each of the `<chapter />` tags, Delphin will search for a corresponding XML file (e.g., for 'debellogallico-4.24', Delphin will search for 'debellogallico-4.24.xml'). The information bracketed by the `<bio />` tag is not currently used in the app. `<title />`, `<heading />` and `<introduction />` correspond to the titles displayed in the app's navigation bar, and on the contents page (compare XML file with the app for details).

An important tag to note here is the `<genre />` tag. If the genre is listed as 'Prose', Delphin expects `<book />`, **`<chapters />`** and **`<chapter />`** tags. Alternatively, if the genre is listed as 'Poetry', Delphin expects `<book />`, **`<passages />`** and **`<passage />`** tags. This is a very important distinction, as it affects how the referenced XML is rendered, as poetry or prose (see next heading for more information).

`<passage />` tags also require two attributes, `start` and `end` indexes, which refer to the line numbers at which the selected passage starts and ends. Because there are not line numbers contained within the referenced XML (see next section), these tags are essential.

#### *[prose]*.xml

```xml
<chapter>
	<sentences>
		<sentence>Ea res ut est Helvetiis per indicium enunciata, moribus suis Orgetorigem ex vinculis causam dicere coegerunt: damnatum poenam sequi oportebat, ut igni cremaretur.</sentence>
		<sentence>Die constituta causae dictionis, Orgetorix ad iudicium omnem suam familiam, ad hominum millia decem, undique coegit et omnes clientes obaeratosque suos, quorum magnum numerum habebat, eodem conduxit: per eos, ne causam diceret, se eripuit.</sentence> 
		<sentence>Cum civitas, ob eam rem incitata, armis ius suum exequi conaretur multitudinemque hominum ex agris magistratus cogerent, Orgetorix mortuus est: neque abest suspicio, ut Helvetii arbitrantur, quin ipse sibi mortem consciverit.</sentence>
	</sentences>

	<notes>
		<note sentence="1" word="8-9">Qui vigent apud nos, ut capitis postulatis non nisi in carcere se purgare liceat. Causam antem dicere, est subire iudicium, et rei, cuius sis postulatus, reddere rationem.</note>
		<note sentence="1" word="16-21">Usitatum hoc erat apud Barbaros supplicium, ut passim ex his libris cognoscitur. Sic in hoc libro Valerius Procillus nihil proprius factum est, quam ut igni a Germanis necaretur. Sed et antiquissimum supplicium fuit apud Orientales. Ita ob scortationem igni Thamar addicitur in lib. Geneseos, et apud Ieremiam tale supplicium sumptum iri de falsis prophetis praedicitur, et apud Danielem pueri a Chaldaeorum rege in fornacem coniciuntur.</note>
		<note sentence="2" word="19-20">Obaerati erant, qui aere alieno obligati erant, ut aliquid operarentur, iique, ut Varro scribit, vindemias et faenisecia exercebant modico aere conducti, quia magno erant obligati, faiseurs de corvées.</note>
	</notes>
</chapter>
```

Prose has two types of text on each page; the original sentences, and the accompanying notes. *All of the markup containing information about which word a note pertains to is contained in the note markup*. Both the `sentence` attribute and the `word` attributes in each note are *zero-indexed*. For example, the first note in the above `<notes />` tag reference the sentence that begins 'Die constituta causae...'.

The `word` attribute (also zero-indexed) is a string of two numbers connected by a hyphen that represents the words to which the note should pertain. The attribute `word="8-9"`, for example, refers to the words 8 through 9 in sentence 1 (moribus suis). If the note only pertains to one word, then the word attribute may also just be a string with a single number. Multiple spreads of words can be referenced by comma separating the spreads (e.g. '8-9,11-14').

#### *[poetry]*.xml

```xml
<passage>
	<lines>
		<line>Primus ibi ante omnes, magna comitante caterva,</line>
		<line>Laocoon ardens summa decurrit ab arce;</line>
		<line>Et procul, O miseri, quae tanta insania, cives?</line>
		<line>Creditis avectos hostes? aut ulla putatis</line>
		<line>Dona carere dolis Danaum? sic notus Ulixes?</line>
		<line>Aut hoc inclusi ligno occultantur Achivi,</line>               
		<line>Aut haec in nostros fabricata est machina muros,</line>
		<line>Inspectura domos, venturaque desuper urbi;</line>
		<line>Aut aliquis latet error; equo ne credite, Teucri.</line>
		<line>Quicquid id est, timeo Danaos et dona ferentes.</line>
		<line>Sic fatus, validis ingentem viribus hastam</line>              
		<line>In latus inque feri curvam compagibus alvum</line>
		<line>Contorsit. Stetit illa tremens, uteroque recusso</line>
		<line>Insonuere cavae gemitumque dedere cavernae.</line>
		<line>Et, si fata Deum, si mens non laeva fuisset.</line>
		<line>Impulerat, ferro Argolicas foedare latebras;</line>    
		<line>Trojaque nunc stares, Priamique arx alta maneres.</line>
	</lines>

	<summaries>
		<summary line="40">Tunc prior coram omnibus Laocoon, magna turba sequente, decurrit celer e summa arce: et procul clamat: O miseri cives! quae tanta est stultitia?</summary>
		<summary line="43">An putatis hostes esse profectos? aut existimatis ulla Graecorum munera career fraudibus? sic Ulysses cognitus est vobis?</summary> 
		<summary line="45">Aut Graeci clausi hoc ligno latent; aut haec machina structa est contra nostra moenia ad explorandum domos, et ex alto ingruendum urbi; aut alius aliquis dolus latet: Troiani, ne fidite huic equo: quodcumque istud est, metuo Gracos, etiam dum munera dant.</summary>
		<summary line="50">Cum haec dixisset, immisit totis viribus magnam hastam in latus, et in uterum equi curvatum juncturis: haesit illa tremens, et repercusso utero cava spatial sonuerunt et emiserunt gemitum.</summary>
		<summary line="54">Et, si fata Deorum, si mens non fuisset sinistra; Laocoon persuasisset, ut violassemus armis Graecas latebras: et nunc stares, o Troia; et maneres, o arx alta Priami.</summary>
	</summaries>

	<notes>
		<note line="41" word="0">Juxta aliquos, Anchisae frater fuit: juxta alios, Priami filius, sacerdos Apollinis: cetera infra, v. 201, 229. De Achivis, Graecis Aen. i. 192.</note>
		<note line="47">Cum enim altior esset muris et domibus, suspicabatur Laocoon esse aut speculam, aut machinam foetam ignibus, qui deinde in subjectam urbem ingruerent.</note>
		<note line="51" word="3">Equi: sic Aen. vii. 409. de cervo: Pectebatque ferum.</note>
		<note line="54" word="7">Fata significat contraria; ut Ge. iv. 7. Numina laeva: mentem vero imprudentem; ut Ecl. i. 16.  ‘ si mens non laeva fuisset.’ Ubi de ambigua vocis hujus potestate fuse agitur.</note>
		<note line="55" word="2,3">Argolicas, Graecas, ab Argis, urbe Peloponnesi, de qua Aen. i. 289. Foedare] Lacerare, vulnerare: ut Aen. iii. 241. ‘obscenas ferro foedare volucres.’</note>
	</notes>
</passage>
```

In contrast to Prose, Poetry XML has **three** sections on each page; the original lines, the prose summaries, and the associated notes. Individual lines are not specifically annotated with line numbers: instead, the line numbers are inferred from the `start` and `end` tags in the XML from which a *[poetry]*.xml file is referenced (see *[author]*.xml above).

Each `<summary />` tag pertains to a series of `<line />` tags. Delphin infers which tags to reference through a single `line` attribute, which refers to *the first line to which the summary refers*. Delphin then takes the difference between this attribute, and the same attribute of the following tag, in order to calculate how many lines should be associated with a summary tag.

`<note />` tags work in exactly the same way as Prose note tags, but with reference to `<line />` tags rather than `<sentence />` tags.


