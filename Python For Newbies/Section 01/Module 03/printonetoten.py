<xml
    xmlns="http://www.w3.org/1999/xhtml">
    <variables>
        <variable type="" id="shT.Xpgt;.{(nc=~l[Za">n</variable>
    </variables>
    <block type="variables_set" x="50" y="49">
        <field name="VAR" id="shT.Xpgt;.{(nc=~l[Za" variabletype="">n</field>
        <value name="VALUE">
            <block type="math_number">
                <field name="NUM">0</field>
            </block>
        </value>
        <next>
            <block type="controls_repeat_ext">
                <value name="TIMES">
                    <block type="math_number">
                        <field name="NUM">10</field>
                    </block>
                </value>
                <statement name="DO">
                    <block type="math_change">
                        <field name="VAR" id="shT.Xpgt;.{(nc=~l[Za" variabletype="">n</field>
                        <value name="DELTA">
                            <shadow type="math_number">
                                <field name="NUM">1</field>
                            </shadow>
                        </value>
                        <next>
                            <block type="text_print">
                                <value name="TEXT">
                                    <block type="variables_get">
                                        <field name="VAR" id="shT.Xpgt;.{(nc=~l[Za" variabletype="">n</field>
                                    </block>
                                </value>
                            </block>
                        </next>
                    </block>
                </statement>
            </block>
        </next>
    </block>
