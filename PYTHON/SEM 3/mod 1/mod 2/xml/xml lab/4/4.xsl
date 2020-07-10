<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html> 
<body>
  <h2>Catalog</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th style="text-align:left">size</th>
      <th style="text-align:left">color_swatch</th>
    </tr>
    <xsl:for-each select="catalog/product">
    <tr>
      <td><xsl:value-of select="size"/></td>
      <td><xsl:value-of select="color_swatch"/></td>
    </tr>
    </xsl:for-each>
  </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

