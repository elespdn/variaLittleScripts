<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
  xpath-default-namespace="http://www.tei-c.org/ns/1.0" xmlns="http://www.tei-c.org/ns/1.0"
  exclude-result-prefixes="xs tei" version="2.0">
  <xsl:output indent="yes"/>



  <!-- copy all -->
  <xsl:template match="@* | node() | comment()" priority="-1">
    <xsl:copy>
      <xsl:apply-templates select="@* | node()"/>
    </xsl:copy>
  </xsl:template>


  <xsl:template match="//l">
    <xsl:variable name="num">
      <xsl:number level="any" count="//l[not(contains(@part, 'F'))]"/>
    </xsl:variable>
    <xsl:element name="{name()}">
      <xsl:choose>
        <xsl:when test="@part = 'F'">
          
        </xsl:when>
        <xsl:otherwise>
          <xsl:attribute name="n">
            <xsl:value-of select="$num"/>
          </xsl:attribute>
        </xsl:otherwise>
      </xsl:choose>

      <xsl:if test="./@part">
        <xsl:attribute name="part">
          <xsl:value-of select="@part"/>
        </xsl:attribute>
      </xsl:if>

      <xsl:value-of select="$num"/>
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>





</xsl:stylesheet>
