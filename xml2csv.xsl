<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:p0112-roud-oeuvres="http://api.knora.org/ontology/0112/roud-oeuvres/xml-import/v1#"
    xmlns:knoraXmlImport="http://api.knora.org/ontology/knoraXmlImport/v1#"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:output encoding="UTF-8" indent="yes" method="text"></xsl:output>
    
    <!-- APPLY TO AUTHORS.XML -->
    
    <xsl:template match="/">
        
        <xsl:for-each select="//p0112-roud-oeuvres:Author">
            <xsl:text>"</xsl:text>
            <xsl:value-of select="./p0112-roud-oeuvres:authorHasFamilyName"/>
            <xsl:text>"; "</xsl:text>
            <xsl:value-of select="./p0112-roud-oeuvres:authorHasGivenName"/>
            <xsl:text>"; "</xsl:text>
            <xsl:value-of select="./@id"/>
            <xsl:text>"&#xa;</xsl:text>  <!-- line break -->
        </xsl:for-each>
        
        
    </xsl:template>
    
    
    
    
    
        
    
    
</xsl:stylesheet>