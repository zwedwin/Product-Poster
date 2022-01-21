

class CoreCommerce_XML:

    @staticmethod
    def cat_add_xml(name, parent):
        xml_string = """
        <Request version="1.0">
            <Authentication>
                <Username>Zach</Username>
                <Password>Fearful4jesuit!</Password>
                <StoreName>mcnulty</StoreName>
                <XMLKey>mcnulty_xml</XMLKey>
            </Authentication>
            <Action>ACTION_TYPE_CATEGORY_ADD</Action>
            <List length="1">
                <Category>
                    <Languages length="2">
                        <LanguageData charset="ISO-8859-1" id="1">
                            <Name>"""+ name +"""</Name>
                            <Teaser></Teaser>
                            <Description></Description>
                            <MetaTitle></MetaTitle>
                            <MetaDescription></MetaDescription>
                            <MetaKeywords></MetaKeywords>
                            <Slug></Slug>
                            <BottomText></BottomText>
                        </LanguageData>
                        <LanguageData charset="UTF-8" id="2">
                            <Name></Name>
                            <Teaser></Teaser>
                            <Description></Description>
                            <MetaTitle></MetaTitle>
                            <MetaDescription></MetaDescription>
                            <MetaKeywords></MetaKeywords>
                            <Slug></Slug>
                            <BottomText></BottomText>
                            </LanguageData>
                        </Languages>
                        <ParentCategory>"""+ parent +"""</ParentCategory>
                        <Sort>0</Sort>
                        <Hide></Hide>
                        <ViewType></ViewType>
                        <GridColumns>3</GridColumns>

                    <CanonicalUrl></CanonicalUrl>
                        <PasswordProtected></PasswordProtected>
                        <SiteWideDiscount>0</SiteWideDiscount>
                        <SlugStyle></SlugStyle>
                        <PhotoGroups length="1">
                            <PhotoGroup>
                                <Photos length="1">
                                    <Photo>
                                        <Flag>THUMBNAIL_PHOTO_FLAG</Flag>
                                        <LocalFile>
                                            <Name></Name>
                                            <Extension></Extension>
                                            <Data></Data>
                                        </LocalFile>
                    <URL></URL>
                        <Width></Width>
                        <Height></Height>
                        <Languages length="2">
                            <LanguageData charset="ISO-8859-1" id="1">
                                <Caption></Caption>
                                <AltTitleTag></AltTitleTag>
                            </LanguageData>
                        <LanguageData charset="UTF-8" id="2">
                            <Caption></Caption>
                            <AltTitleTag></AltTitleTag>
                        </LanguageData>
                    </Languages>
                </Photo>
            </Photos>
        </PhotoGroup>
    </PhotoGroups>
</Category>
</List>
</Request>
    """
        return xml_string

#this xml request is not currently used but could be in future versions of product add funcationality
#this xml is also obviously very long (~1000 lines) and will make product posting more reliable but will take a long time to get right
    @staticmethod
    def product_add_xml():
        xml_string = """
        <Request version="1.0">
              <Authentication>
                  <Username><![CDATA[admin]]></Username>
                  <Password><![CDATA[Password1!]]></Password>
                  <StoreName><![CDATA[sumeffectsof224]]></StoreName>
                  <XMLKey><![CDATA[123]]></XMLKey>
              </Authentication>
              <Action>ACTION_TYPE_PRODUCT_ADD</Action>
              <List length="1">
                  <Product>
                      <Languages length="2">
                          <LanguageData charset="ISO-8859-1" id="1">
                          <Name><![CDATA[Test Product]]></Name>
                              <Teaser><![CDATA[Teaser]]></Teaser>
                              <Description><![CDATA[Description]]></Description>
                              <CallEmailForPricingDisplay><![CDATA[Call/Email For Pricing]]></CallEmailForPricingDisplay>
                              <MetaTitle><![CDATA[Meta Title]]></MetaTitle>
                              <MetaDescription><![CDATA[Meta Description]]></MetaDescription>
                              <MetaKeywords><![CDATA[Meta Keywords]]></MetaKeywords>
                              <MobileTeaser><![CDATA[Mobile Teaser]]></MobileTeaser>
                              <MobileDescription><![CDATA[Mobile Description]]></MobileDescription>
                              <CustomTab1Name><![CDATA[Details]]></CustomTab1Name>
                              <CustomTab1HTML><![CDATA[Handles Extremely Well:<br/><ul><li>Under water</li><li>High temperatures</li><li>Low temperatures</li></ul>]]></CustomTab1HTML>
                              <CustomTab2Name><![CDATA[Warranty]]></CustomTab2Name>
                              <CustomTab2HTML><![CDATA[Comes with standard 2 year mfg warranty.]]></CustomTab2HTML>
                              <Slug><![CDATA[custom_slug]]></Slug>
                          </LanguageData>
                          <LanguageData charset="UTF-8" id="2">
                              <Name><![CDATA[Test Product (greek)]]></Name>
                              <Teaser><![CDATA[Teaser (greek)]]></Teaser>
                              <Description><![CDATA[Description (greek)]]></Description>
                              <CallEmailForPricingDisplay><![CDATA[Call/Email For Pricing(greek)]]></CallEmailForPricingDisplay>
                              <MetaTitle><![CDATA[Meta Title (greek)]]></MetaTitle>
                              <MetaDescription><![CDATA[Meta Description (greek)]]></MetaDescription>
                              <MetaKeywords><![CDATA[Meta Keywords (greek)]]></MetaKeywords>
                              <MobileTeaser><![CDATA[Mobile Teaser (greek)]]></MobileTeaser>
                              <MobileDescription><![CDATA[Mobile Description (greek)]]></MobileDescription>
                              <CustomTab1Name><![CDATA[Details (greek)]]></CustomTab1Name>
                              <CustomTab1HTML><![CDATA[Handles Extremely Well (greek):<br/><ul><li>Under water</li><li>High temperatures</li><li>Lowtemperatures</li></ul>]]></CustomTab1HTML>
                              <CustomTab2Name><![CDATA[Warranty (greek)]]></CustomTab2Name>
                              <CustomTab2HTML><![CDATA[Comes with standard 2 year mfg warranty. (greek)]]></CustomTab2HTML>
                              <Slug><![CDATA[custom_slug_greek]]></Slug>
                          </LanguageData>
                      </Languages>
                      <SKU><![CDATA[sku-1]]></SKU>
                      <UPC><![CDATA[upc-1]]></UPC>
                      <MSRP>
                          <Amount><![CDATA[2.50]]></Amount>
                      </MSRP>
                      <Price>
                          <Amount><![CDATA[5.00]]></Amount>
                      </Price>
                      <SalesPrice>
                          <Amount><![CDATA[2.00]]></Amount>
                      </SalesPrice>
                      <SaleStart>
                          <UnixTimeStamp>1281675600</UnixTimeStamp>
                          <Day>13</Day>
                          <Month>08</Month>
                          <Year>2010</Year>
                          <Hour>00</Hour>
                          <Minute>00</Minute>
                          <Second>00</Second>
                      </SaleStart>
                      <SaleEnd>
                          <UnixTimeStamp>1281675600</UnixTimeStamp>
                          <Day>13</Day>
                          <Month>08</Month>
                          <Year>2010</Year>
                          <Hour>00</Hour>
                          <Minute>00</Minute>
                          <Second>00</Second>
                      </SaleEnd>
                      <UseSalesPrice>Boolean Types</UseSalesPrice>
                      <CustomerMustAddToCartToSeeSalesPrice>BooleanTypes</CustomerMustAddToCartToSeeSalesPrice>
                      <DisplayMSRPAndSavingsFormat>Boolean Types</DisplayMSRPAndSavingsFormat>
                      <Categories length="1">
                          <Category>
                              <Languages length="2">
                                  <LanguageData charset="ISO-8859-1" id="1">
                                      <Name><![CDATA[Test Category]]></Name>
                                  </LanguageData>
                                  <LanguageData charset="UTF-8" id="2">
                                      <Name><![CDATA[Test Category (greek)]]></Name>
                                  </LanguageData>
                              </Languages>
                          </Category>
                      </Categories>
                      <Vendors length="1">
                          <Vendor id="1">
                              <Company><![CDATA[Test Vendor]]></Company>
                          </Vendor>
                      </Vendors>
                      <DisplayFacebookLink>Boolean Types</DisplayFacebookLink>
                      <DisplayTwitterLink>Boolean Types</DisplayTwitterLink>
                      <CustomProductLists length="1">
                          <CustomProductList id="1">
                              <Name><![CDATA[Test Custom Product List]]></Name>
                              <ListItems length="1">
                                  <ListItem id="1">
                                      <Name><![CDATA[Test Custom Product List Item]]></Name>
                                  </ListItem>
                              </ListItems>
                          </CustomProductList>
                      </CustomProductLists>
                      <TwoCheckoutId><![CDATA[111]]></TwoCheckoutId>
                      <GoogleWebsiteOptimizer>
                          <Enabled>Boolean Types</Enabled>
                          <TestVariants length="1">
                              <TestVariant>Google Website Optimizer Variant Types</TestVariant>
                          </TestVariants>
                      </GoogleWebsiteOptimizer>
                      <Available>Boolean Types</Available>
                      <Discontinued>Boolean Types</Discontinued>
                      <TrackInventory>Product Inventory Tracking Types</TrackInventory>
                      <InventoryLevel><![CDATA[5]]></InventoryLevel>
                      <LowInventoryNotifyLevel><![CDATA[2]]></LowInventoryNotifyLevel>
                      <InventoryNotified>Boolean Types</InventoryNotified>
                      <Cost>
                          <Amount><![CDATA[1.50]]></Amount>
                      </Cost>
                      <BundledProducts length="1">
                          <BundledProduct id="1">
                              <Languages length="2">
                                  <LanguageData charset="ISO-8859-1" id="1">
                                      <Name><![CDATA[Bundled Product]]></Name>
                                  </LanguageData>
                                  <LanguageData charset="UTF-8" id="2">
                                      <Name><![CDATA[Bundled Product (german)]]></Name>
                                  </LanguageData>
                              </Languages>
                          </BundledProduct>
                      </BundledProducts>
                      <BundleDiscount>5</BundleDiscount>
                      <Weight>
                          <Amount><![CDATA[5]]></Amount>
                          <Units>LBS/KGS/OZ</Units>
                      </Weight>
                      <BoxWidth><![CDATA[5.00]]></BoxWidth>
                      <BoxHeight><![CDATA[6.00]]></BoxHeight>
                      <BoxLength><![CDATA[7.00]]></BoxLength>
                      <BoxGirth><![CDATA[8.00]]></BoxGirth>
                      <FirstClassMailType>USPS First Class Mail Types</FirstClassMailType>
                      <ContainerType>USPS Container Types</ContainerType>
                      <MultiShipBox>Y/N</MultiShipBox>
                      <Weight2>
                          <Amount><![CDATA[5]]></Amount>
                          <Units>LBS/KGS/OZ</Units>
                      </Weight2>
                      <Width2><![CDATA[5.00]]></Width2>
                      <Height2><![CDATA[6.00]]></Height2>
                      <Length2><![CDATA[7.00]]></Length2>
                      <BoxGirth2><![CDATA[8.00]]></BoxGirth2>
                      <FirstClassMailType2>USPS First Class Mail Types</FirstClassMailType2>
                      <ContainerType2>USPS Container Types</ContainerType2>
                      <Weight3>
                          <Amount><![CDATA[5]]></Amount>
                          <Units>LBS/KGS/OZ</Units>
                      </Weight3>
                      <Width3><![CDATA[5.00]]></Width3>
                      <Height3><![CDATA[6.00]]></Height3>
                      <Length3><![CDATA[7.00]]></Length3>
                      <BoxGirth3><![CDATA[8.00]]></BoxGirth3>
                      <FirstClassMailType3>USPS First Class Mail Types</FirstClassMailType3>
                      <ContainerType3>USPS Container Types</ContainerType3>
                      <Weight4>
                          <Amount><![CDATA[5]]></Amount>
                          <Units>LBS/KGS/OZ</Units>
                      </Weight4>
                      <Width4><![CDATA[5.00]]></Width4>
                      <Height4><![CDATA[6.00]]></Height4>
                      <Length4><![CDATA[7.00]]></Length4>
                      <BoxGirth4><![CDATA[8.00]]></BoxGirth4>
                      <FirstClassMailType4>USPS First Class Mail Types</FirstClassMailType4>
                      <ContainerType4>USPS Container Types</ContainerType4>
                      <Weight5>
                          <Amount><![CDATA[5]]></Amount>
                          <Units>LBS/KGS/OZ</Units>
                      </Weight5>
                      <Width5><![CDATA[5.00]]></Width5>
                      <Height5><![CDATA[6.00]]></Height5>
                      <Length5><![CDATA[7.00]]></Length5>
                      <BoxGirth5><![CDATA[8.00]]></BoxGirth5>
                      <FirstClassMailType5>USPS First Class Mail Types</FirstClassMailType5>
                      <ContainerType5>USPS Container Types</ContainerType5>
                      <FreightClass>Freight Classes</FreightClass>
                      <SouthEasternFreightClass>South Eastern Freight Classes</SouthEasternFreightClass>
                      <ABFFreightClass>ABF Freight Classes</ABFFreightClass>
                      <UPSFreightClass>UPS Freight Classes</UPSFreightClass>
                      <UPSFreightNumberOfPieces><![CDATA[4]]></UPSFreightNumberOfPieces>
                      <UPSFreightNumberOfHandlingUnits><![CDATA[0.75]]></UPSFreightNumberOfHandlingUnits>
                      <UPSFreightPackaging>UPS Freight Packaging Types</UPSFreightPackaging>
                      <ShippingSurcharge>
                          <Amount><![CDATA[.33]]></Amount>
                      </ShippingSurcharge>
                      <FreightItem>
                          <Amount><![CDATA[5.00]]></Amount>
                      </FreightItem>
                      <PerProductShipping>
                          <Options length="2">
                              <Option zoneId="1">
                                  <ShippingOption><![CDATA[Option 1]]></ShippingOption>
                                  <PricePerQuantity>
                                      <Amount><![CDATA[1.50]]></Amount>
                                  </PricePerQuantity>
                                  <NotApplicable>Boolean Types</NotApplicable>
                              </Option>
                          </Options>
                      </PerProductShipping>
                      <RelatedProducts length="1">
                          <RelatedProduct id="1">
                              <Languages>
                                  <LanguageData charset="ISO-8859-1" id="1">
                                      <Name><![CDATA[Related Product]]></Name>
                                  </LanguageData>
                                  <LanguageData charset="UTF-8" id="2">
                                      <Name><![CDATA[Related Product (greek)]]></Name>
                                  </LanguageData>
                              </Languages>
                          </RelatedProduct>
                      </RelatedProducts>
                      <NumberOfRelatedProductsToDisplay><![CDATA[5]]></NumberOfRelatedProductsToDisplay>
                      <CrossSellProducts length="1">
                          <CrossSellProduct id="1">
                              <Languages>
                                  <LanguageData charset="ISO-8859-1" id="1">
                                      <Name><![CDATA[Cross Sell Product]]></Name>
                                  </LanguageData>
                                  <LanguageData charset="UTF-8" id="2">
                                      <Name><![CDATA[Cross Sell Product (greek)]]></Name>
                                  </LanguageData>
                              </Languages>
                          </CrossSellProduct>
                      </CrossSellProducts>
                      <Size><![CDATA[1"x2"x3"]]></Size>
                      <CallEmailForPricing>Boolean Types</CallEmailForPricing>
                      <CallEmailForPricingDisplayPrice>Boolean Types</CallEmailForPricingDisplayPrice>
                      <UserDefinedFields length="2">
                          <UserDefinedField>
                              <Label><![CDATA[UDF 1]]></Label>
                              <Value><![CDATA[UDF Value 1]]></Value>
                          </UserDefinedField>
                          <UserDefinedField>
                              <Label><![CDATA[UDF 2]]></Label>
                              <Value><![CDATA[UDF Value 2]]></Value>
                          </UserDefinedField>
                      </UserDefinedFields>
                      <Personalizations length="1">
                           <Question>
                               <Languages>
                                   <LanguageData charset="ISO-8859-1" id="1">
                                       <Name><![CDATA[Question 1]]></Name>
                                       <HelperText><![CDATA[Answer this question to the best of your ability]]></HelperText>
                                   </LanguageData>
                                   <LanguageData charset="UTF-8" id="2">
                                       <Name><![CDATA[Question 1 (greek)]]></Name>
                                       <HelperText><![CDATA[Answer this question to the best of your ability in Greek]]></HelperText>
                                   </LanguageData>
                               </Languages>
                               <Type>Personalization Types</Type>
                               <Size><![CDATA[5]]></Size>
                               <MaxCharacters><![CDATA[15]]></MaxCharacters>
                               <Required>Boolean Types</Required>
                               <SortOrder><![CDATA[1]]></SortOrder>
                               <TrackInventory>Boolean Types</TrackInventory>
                               <Enabled>Boolean Types</Enabled>
                               <Answers length="1">
                                   <Answer id="1">
                                       <Languages length="2">
                                           <LanguageData charset="ISO-8859-1" id="1">
                                               <Name><![CDATA[Answer 1]]></Name>
                                           </LanguageData>
                                           <LanguageData charset="UTF-8" id="2">
                                               <Name><![CDATA[Answer 1 (greek)]]></Name>
                                           </LanguageData>
                                       </Languages>
                                       <Price>
                                           <Amount><![CDATA[2.00]]></Amount>
                                       </Price>
                                       <CustomPricing type="Customer Group Discount Types">
                                           <CustomerGroupPricing>
                                               <CustomerGroups length="2">
                                                   <CustomerGroup id="1">
                                                       <Name><![CDATA[Customer Group 1]]></Name>
                                                       <Price>
                                                           <Amount><![CDATA[10.00]]></Amount>
                                                       </Price>
                                                   </CustomerGroup>
                                                   <CustomerGroup id="2">
                                                       <Name><![CDATA[Customer Group 2]]></Name>
                                                       <Price>
                                                           <Amount><![CDATA[15.00]]></Amount>
                                                       </Price>
                                                   </CustomerGroup>
                                               </CustomerGroups>
                                           </CustomerGroupPricing>
                                       </CustomPricing>
                                       <SKU><![CDATA[abc-123]]></SKU>
                                       <Enabled>Boolean Types</Enabled>
                                       <Default>Boolean Types</Default>
                                       <SortOrder><![CDATA[1]]></SortOrder>
                                       <PriceType>Product Personalization Answer Price Types</PriceType>
                                       <Weight>
                                           <Amount><![CDATA[5]]></Amount>
                                           <Units>Weight Units</Units>
                                       </Weight>
                                       <Cost>
                                           <Amount><![CDATA[1.25]]></Amount>
                                       </Cost>
                                       <InventoryLevel><![CDATA[5]]></InventoryLevel>
                                       <LowInventoryNotifyLevel><![CDATA[2]]></LowInventoryNotifyLevel>
                                   </Answer>
                               </Answers>
                           </Question>
                       </Personalizations>
                      <PhotoGroups length="1">
                          <PhotoGroup id="1">
                              <Photos length="1">
                                  <Photo id="1">
                                      <Flag>Photo Flags</Flag>
                                      <LocalFile>
                                          <Name><![CDATA[mytest.jpg]]></Name>
                                          <Extension><![CDATA[jpg]]></Extension>
                                          <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                                      </LocalFile>
                                      <URL><![CDATA[1]]></URL>
                                      <CopyPhoto><![CDATA[TRUE_VALUE]]></CopyPhoto>
                                      <Width><![CDATA[100]]></Width>
                                      <Height><![CDATA[200]]></Height>
                                      <Languages length="2">
                                          <LanguageData charset="ISO-8859-1" id="1">
                                              <Caption><![CDATA[Caption 1]]></Caption>
                                              <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                                          </LanguageData>
                                          <LanguageData charset="UTF-8" id="2">
                                              <Caption><![CDATA[Caption 1 (greek)]]></Caption>
                                              <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                                          </LanguageData>
                                      </Languages>
                                  </Photo>
                                  <SortOrder></SortOrder>
                              </Photos>
                          </PhotoGroup>
                      </PhotoGroups>
                      <OptionGroups length="2">
                           <OptionGroup id="1">
                               <Languages length="2">
                                   <LanguageData charset="ISO-8859-1" id="1">
                                       <Name><![CDATA[Size]]></Name>
                                       <FirstOptionValue><![CDATA[Please Choose a Size]]></FirstOptionValue>                        </LanguageData>
                                   <LanguageData cahrset="UTF-8" id="2">
                                       <Name><![CDATA[Size (greek)]]></Name>
                                       <FirstOptionValue><![CDATA[Please Choose a Size
            (greek)]]></FirstOptionValue>
                                   </LanguageData>
                               </Languages>
                               <UseFirstOptionValue>Boolean Types</UseFirstOptionValue>
                               <SortOrder><![CDATA[1]]></SortOrder>
                               <Options length="2">
                                   <Option id="1">
                                       <Languages length="2">
                                           <LanguageData charset="ISO-8859-1" id="1">
                                               <Name><![CDATA[Small]]></Name>
                                           </LanguageData>
                                           <LanguageData cahrset="UTF-8" id="2">
                                               <Name><![CDATA[Small (greek)]]></Name>
                                           </LanguageData>
                                       </Languages>
                                       <SortOrder><![CDATA[2]]></SortOrder>
                                       <SKU><![CDATA[abc-123]]></SKU>
                                       <Price>
                                           <Amount><![CDATA[5.00]]></Amount>
                                       </Price>
                                       <Weight>
                                           <Amount><![CDATA[5]]></Amount>
                                           <Units>Weight Units</Units>
                                       </Weight>
                                       <Cost>
                                           <Amount><![CDATA[2.50]]></Amount>
                                       </Cost>
                                       <MSRP>
                                           <Amount><![CDATA[6.00]]></Amount>
                                       </MSRP>
                                       <Photos length="1">
                                           <Photo id="1">
                                               <Flag>Photo Flags</Flag>
                                               <LocalFile>
                                                   <Name><![CDATA[mytest.jpg]]></Name>
                                                   <Extension><![CDATA[jpg]]></Extension>
                                                   <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                                               </LocalFile>
                                               <URL><![CDATA[http://www.mysite.com/myimage.jpg]]></URL>
                                               <Width><![CDATA[100]]></Width>
                                               <Height><![CDATA[200]]></Height>
                                               <Languages length="2">
                                                   <LanguageData charset="ISO-8859-1" id="1">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                                                   </LanguageData>
                                                   <LanguageData charset="UTF-8" id="2">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                                                   </LanguageData>
                                               </Languages>
                                               <AltLocation><![CDATA[http://www.corecommerce.com]]></AltLocation>
                                           </Photo>
                                       </Photos>
                                   </Option>
                                   <Option id="2">
                                       <Languages length="2">
                                           <LanguageData charset="ISO-8859-1" id="1">
                                               <Name><![CDATA[Medium]]></Name>
                                           </LanguageData>
                                           <LanguageData cahrset="UTF-8" id="2">
                                               <Name><![CDATA[Medium (greek)]]></Name>
                                           </LanguageData>
                                       </Languages>
                                       <SortOrder><![CDATA[2]]></SortOrder>
                                       <SKU><![CDATA[abc-123]]></SKU>
                                       <Price>
                                           <Amount><![CDATA[5.00]]></Amount>
                                       </Price>
                                       <Weight>
                                           <Amount><![CDATA[5]]></Amount>
                                           <Units>Weight Units</Units>
                                       </Weight>
                                       <Cost>
                                           <Amount><![CDATA[2.50]]></Amount>
                                       </Cost>
                                       <MSRP>
                                           <Amount><![CDATA[6.00]]></Amount>
                                       </MSRP>
                                       <Photos length="1">
                                           <Photo id="2">
                                               <Flag>Photo Flags</Flag>
                                               <LocalFile>
                                                   <Name><![CDATA[mytest.jpg]]></Name>
                                                   <Extension><![CDATA[jpg]]></Extension>
                                                   <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                                               </LocalFile>
                                               <URL><![CDATA[http://www.mysite.com/myimage.jpg]]></URL>
                                               <Width><![CDATA[100]]></Width>
                                               <Height><![CDATA[200]]></Height>
                                               <Languages length="2">
                                                   <LanguageData charset="ISO-8859-1" id="1">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                                                   </LanguageData>
                                                   <LanguageData charset="UTF-8" id="2">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                                                   </LanguageData>
                                               </Languages>
                                                    <AltLocation><![CDATA[http://www.corecommerce.com]]></AltLocation>
                                           </Photo>
                                       </Photos>
                                   </Option>
                               </Options>
                           </OptionGroup>
                           <OptionGroup id="2">
                               <Languages length="2">
                                   <LanguageData charset="ISO-8859-1" id="1">
                                       <Name><![CDATA[Color]]></Name>
                                       <FirstOptionValue><![CDATA[Please Choose a Color]]></FirstOptionValue>
                                   </LanguageData>
                                   <LanguageData cahrset="UTF-8" id="2">
                                       <Name><![CDATA[Color (greek)]]></Name>
                                       <FirstOptionValue><![CDATA[Please Choose a Color(greek)]]></FirstOptionValue>
                                   </LanguageData>
                               </Languages>
                               <UseFirstOptionValue>Boolean Types</UseFirstOptionValue>
                               <SortOrder><![CDATA[2]]></SortOrder>
                               <Options length="2">
                                   <Option id="3">
                                       <Languages length="2">
                                           <LanguageData charset="ISO-8859-1" id="1">
                                               <Name><![CDATA[Yellow]]></Name>
                                           </LanguageData>
                                           <LanguageData cahrset="UTF-8" id="2">
                                               <Name><![CDATA[Yellow (greek)]]></Name>
                                           </LanguageData>
                                       </Languages>
                                       <SortOrder><![CDATA[2]]></SortOrder>
                                       <SKU><![CDATA[abc-123]]></SKU>
                                       <Price>
                                           <Amount><![CDATA[5.00]]></Amount>
                                       </Price>
                                       <Weight>
                                           <Amount><![CDATA[5]]></Amount>
                                           <Units>Weight Units</Units>
                                       </Weight>
                                       <Cost>
                                           <Amount><![CDATA[2.50]]></Amount>
                                       </Cost>
                                       <MSRP>
                                           <Amount><![CDATA[6.00]]></Amount>
                                       </MSRP>
                                       <Photos length="1">
                                           <Photo id="3">
                                               <Flag>Photo Flags</Flag>
                                               <LocalFile>
                                                   <Name><![CDATA[mytest.jpg]]></Name>
                                                   <Extension><![CDATA[jpg]]></Extension>
                                                   <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                                               </LocalFile>
                                               <URL><![CDATA[http://www.mysite.com/myimage.jpg	]]><	/URL>
                                   <CopyPhoto><![CDATA[TRUE_VALUE]]></CopyPhoto>
                                               <Width><![CDATA[100]]></Width>
                                               <Height><![CDATA[200]]></Height>
                                               <Languages length="2">
                                                   <LanguageData charset="ISO-8859-1" id="1">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                                                   </LanguageData>
                                                   <LanguageData charset="UTF-8" id="2">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                                                   </LanguageData>
                                               </Languages>
                                               <AltLocation><![CDATA[http://www.corecommerce.com]]></AltLocation>
                                           </Photo>
                                       </Photos>
                                   </Option>
                                   <Option id="4">
                                       <Languages length="2">
                                           <LanguageData charset="ISO-8859-1" id="1">
                                               <Name><![CDATA[Orange]]></Name>
                                           </LanguageData>
                                           <LanguageData cahrset="UTF-8" id="2">
                                               <Name><![CDATA[Orange (greek)]]></Name>
                                           </LanguageData>
                                       </Languages>
                                       <SortOrder><![CDATA[2]]></SortOrder>
                                       <SKU><![CDATA[abc-123]]></SKU>
                                       <Price>
                                           <Amount><![CDATA[5.00]]></Amount>
                                       </Price>
                                       <Weight>
                                           <Amount><![CDATA[5]]></Amount>
                                           <Units>Weight Units</Units>
                                       </Weight>
                                       <Cost>
                                           <Amount><![CDATA[2.50]]></Amount>
                                       </Cost>
                                       <MSRP>
                                           <Amount><![CDATA[6.00]]></Amount>
                                       </MSRP>
                                       <Photos length="1">
                                           <Photo id="4">
                                               <Flag>Photo Flags</Flag>
                                               <LocalFile>
                                                   <Name><![CDATA[mytest.jpg]]></Name>
                                                   <Extension><![CDATA[jpg]]></Extension>
                                                   <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                                               </LocalFile>
                                               <URL><![CDATA[http://www.mysite.com/myimage.jpg]]></URL>
                                               <Width><![CDATA[100]]></Width>
                                               <Height><![CDATA[200]]></Height>
                                               <Languages length="2">
                                                   <LanguageData charset="ISO-8859-1" id="1">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                                                   </LanguageData>
                                                   <LanguageData charset="UTF-8" id="2">
                                                       <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                                                   </LanguageData>
                                               </Languages>
                                               <AltLocation><![CDATA[http://www.corecommerce.com]]></AltLocation>
                                           </Photo>
                                       </Photos>
                                   </Option>
                               </Options>
                           </OptionGroup>
                       </OptionGroups>
                       <OptionSets length="1">
                           <OptionSet id="1">
                               <Groups length="2">
                                   <Group>
                                       <LanguageData charset="ISO-8859-1" id="1">
                                           <GroupName><![CDATA[Size]]></GroupName>
                                           <OptionName><![CDATA[Medium]]></OptionName>
                                       </LanguageData>
                                   </Group>
                                   <Group>
                                       <LanguageData charset="ISO-8859-1" id="1">
                                           <GroupName><![CDATA[Color]]></GroupName>
                                           <OptionName><![CDATA[Yellow]]></OptionName>
                                       </LanguageData>
                                   </Group>
                               </Groups>
                               <SKU><![CDATA[abc-123]]></SKU>
                               <Price>
                                   <Amount><![CDATA[1.00]]></Amount>
                               </Price>
                               <Weight>
                                   <Amount><![CDATA[5.00]]></Amount>
                                   <Units>Weight Units</Units>
                               </Weight>
                               <Cost>
                                   <Amount><![CDATA[.75]]></Amount>
                               </Cost>
                               <MSRP>
                                   <Amount><![CDATA[6.00]]></Amount>
                               </MSRP>
                               <DownloadFile>
                                   <Name><![CDATA[download1.zip]]></Name>
                                   <Extension><![CDATA[zip]]></Extension>
                                   <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                               </DownloadFile>
                               <Enabled>Boolean Types</Enabled>
                               <InventoryLevel>10</InventoryLevel>
                               <LowInventoryNotifyLevel>5</LowInventoryNotifyLevel>
                               <Photos length="1">
                                   <Photo id="5">
                                       <Flag>Photo Flags</Flag>
                                       <LocalFile>
                                           <Name><![CDATA[mytest.jpg]]></Name>
                                           <Extension><![CDATA[jpg]]></Extension>
                                           <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                                       </LocalFile>
                                       <URL><![CDATA[http://www.mysite.com/myimage.jpg]]></URL>
                                       <Width><![CDATA[100]]></Width>
                                       <Height><![CDATA[200]]></Height>
                                       <Languages length="2">
                                           <LanguageData charset="ISO-8859-1" id="1">
                                               <Caption><![CDATA[Caption 1]]></Caption>
                                               <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                                           </LanguageData>
                                           <LanguageData charset="UTF-8" id="2">
                                               <Caption><![CDATA[Caption 1 (greek)]]></Caption>
                                               <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                                           </LanguageData>
                                       </Languages>
                                   </Photo>
                               </Photos>
                           </OptionSet>
                       </OptionSets>
                       <CustomPricing type="Customer Group Discount Types">
                          <CustomerGroupPricing>
                              <CustomerGroups length="2">
                                  <CustomerGroup id="1">
                                      <Name><![CDATA[Customer Group 1]]></Name>
                                      <Price>
                                          <Amount><![CDATA[10.00]]></Amount>
                                      </Price>
                                  </CustomerGroup>
                                  <CustomerGroup id="2">
                                      <Name><![CDATA[Customer Group 2]]></Name>
                                      <Price>
                                          <Amount><![CDATA[15.00]]></Amount>
                                      </Price>
                                  </CustomerGroup>
                              </CustomerGroups>
                          </CustomerGroupPricing>
                          <QuantityBasedPricing>
                              <QuantityGroups length="2">
                                  <QuantityGroup>
                                      <Minimum><![CDATA[1]]></Minimum>
                                      <Maximum><![CDATA[5]]></Maximum>
                                      <Price>
                                          <Amount><![CDATA[5.00]]></Amount>
                                      </Price>
                                      <CustomerGroupPrices length="2">
                                          <CustomerGroupPrice id="1">
                                              <Name><![CDATA[Customer Group 1]]></Name>
                                              <Price>
                                                  <Amount><![CDATA[1.00]]></Amount>
                                              </Price>
                                          </CustomerGroupPrice>
                                          <CustomerGroupPrice id="2">
                                              <Name><![CDATA[Customer Group 2]]></Name>
                                              <Price>
                                                  <Amount><![CDATA[2.00]]></Amount>
                                              </Price>
                                          </CustomerGroupPrice>
                                      </CustomerGroupPrices>
                                  </QuantityGroup>
                                  <QuantityGroup>
                                      <Minimum><![CDATA[6]]></Minimum>
                                      <Maximum><![CDATA[10]]></Maximum>
                                      <Price>
                                          <Amount><![CDATA[3.00]]></Amount>
                                      </Price>
                                      <CustomerGroupPrices length="2">
                                          <CustomerGroupPrice id="1">
                                              <Name><![CDATA[Customer Group 1]]></Name>
                                              <Price>
                                                  <Amount><![CDATA[3.00]]></Amount>
                                              </Price>
                                          </CustomerGroupPrice>
                                          <CustomerGroupPrice id="2">
                                              <Name><![CDATA[Customer Group 2]]></Name>
                                              <Price>
                                                  <Amount><![CDATA[4.00]]></Amount>
                                              </Price>
                                          </CustomerGroupPrice>
                                      </CustomerGroupPrices>
                                  </QuantityGroup>
                              </QuantityGroups>
                          </QuantityBasedPricing>
                      </CustomPricing>
                      <DownloadFiles length="2">
                          <DownloadFile>
                              <Name><![CDATA[download1.zip]]></Name>
                              <Extension><![CDATA[zip]]></Extension>
                              <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                          </DownloadFile>
                          <DownloadFile>
                              <Name><![CDATA[download2.zip]]></Name>
                              <Extension><![CDATA[zip]]></Extension>
                              <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                          </DownloadFile>
                      </DownloadFiles>
                      <Taxable>Boolean Types</Taxable>
                      <Featured>Boolean Types</Featured>
                      <ShippingExempt>Boolean Types</ShippingExempt>
                      <EligibleForFreeShipping>Boolean Types</EligibleForFreeShipping>
                      <GiftWrappingAvailable>Boolean Types</GiftWrappingAvailable>
                      <EligibleForRewardPoints>Boolean Types</EligibleForRewardPoints>
                      <AllowFileUploads>Boolean Types</AllowFileUploads>
                      <EligibleForSubscriptionBilling>Boolean Types</EligibleForSubscriptionBilling>
                      <SubscriptionPrice>
                          <Amount><![CDATA[5.00]]></Amount>
                      </SubscriptionPrice>
                      <UseEmailReminder>Boolean Types</UseEmailReminder>
                      <EmailReminders length="2">
                          <EmailReminder>
                              <Default>Boolean Types</Default>
                              <Available>Boolean Types</Available>
                              <Name>Email Reminder Names</Name>
                          </EmailReminder>
                          <EmailReminder>
                              <Default>Boolean Types</Default>
                              <Available>Boolean Types</Available>
                              <Name>Email Reminder Names</Name>
                          </EmailReminder>
                      </EmailReminders>
                      <MinimumOrderQuantity><![CDATA[5]]></MinimumOrderQuantity>
                      <SubscriptionShippingFee>
                          <Amount><![CDATA[5.00]]></Amount>
                      </SubscriptionShippingFee>
                      <AllowSubscriptionLimit>Boolean Types</AllowSubscriptionLimit>
                      <SubscriptionLimit><![CDATA[5]]></SubscriptionLimit>
                      <Condition>Froogle Condition Types</Condition>
                      <Expiration>
                          <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                          <Day><![CDATA[2]]></Day>
                          <Month><![CDATA[5]]></Month>
                          <Year><![CDATA[2009]]></Year>
                          <Hour><![CDATA[12]]></Hour>
                          <Minute><![CDATA[22]]></Minute>
                          <Second><![CDATA[33]]></Second>
                      </Expiration>
                      <ProductType><![CDATA[Product Type]]></ProductType>
                      <ISBN><![CDATA[1234567890]]></ISBN>
                      <EmailAutoResponders length="2">
                          <EmailAutoResponder id="1">
                              <Languages length="2">
                                  <LanguageData charset="ISO-8859-1" id="1">
                                      <Name><![CDATA[Auto Responder 1]]></Name>
                                  </LanguageData>
                                  <LanguageData charset="UTF-8" id="2">
                                      <Name><![CDATA[Auto Responder 1 (greek)]]></Name>
                                  </LanguageData>
                              </Languages>
                          </EmailAutoResponder>
                          <EmailAutoResponder id="2">
                              <Languages length="2">
                                  <LanguageData charset="ISO-8859-1" id="1">
                                      <Name><![CDATA[Auto Responder 2]]></Name>
                                  </LanguageData>
                                  <LanguageData charset="UTF-8" id="2">
                                      <Name><![CDATA[Auto Responder 2 (greek)]]></Name>
                                  </LanguageData>
                              </Languages>
                          </EmailAutoResponder>
                      </EmailAutoResponders>
                      <Shopzilla>
                          <CategoryIdentification><![CDATA[Category Id]]></CategoryIdentification>
                          <Condition>Shopzilla Condition Types</Condition>
                      </Shopzilla>
                      <CouponsAvailable length="2">
                          <Coupon id="1">
                              <Code><![CDATA[Coupon 1]]></Code>
                              <StartDate>
                                  <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                                  <Day><![CDATA[2]]></Day>
                                  <Month><![CDATA[5]]></Month>
                                  <Year><![CDATA[2009]]></Year>
                                  <Hour><![CDATA[12]]></Hour>
                                  <Minute><![CDATA[22]]></Minute>
                                  <Second><![CDATA[33]]></Second>
                              </StartDate>
                              <Expiration>
                                  <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                                  <Day><![CDATA[2]]></Day>
                                  <Month><![CDATA[10]]></Month>
                                  <Year><![CDATA[2009]]></Year>
                                  <Hour><![CDATA[12]]></Hour>
                                  <Minute><![CDATA[22]]></Minute>
                                  <Second><![CDATA[33]]></Second>
                              </Expiration>
                              <Discount>
                                  <Amount><![CDATA[10.00]]></Amount>
                              </Discount>
                          </Coupon>
                          <Coupon id="2">
                              <Code><![CDATA[Coupon 2]]></Code>
                              <StartDate>
                                  <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                                  <Day><![CDATA[2]]></Day>
                                  <Month><![CDATA[5]]></Month>
                                  <Year><![CDATA[2009]]></Year>
                                  <Hour><![CDATA[12]]></Hour>
                                  <Minute><![CDATA[22]]></Minute>
                                  <Second><![CDATA[33]]></Second>
                              </StartDate>
                              <Expiration>
                                  <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                                  <Day><![CDATA[2]]></Day>
                                  <Month><![CDATA[10]]></Month>
                                  <Year><![CDATA[2009]]></Year>
                                  <Hour><![CDATA[12]]></Hour>
                                  <Minute><![CDATA[22]]></Minute>
                                  <Second><![CDATA[33]]></Second>
                              </Expiration>
                              <Discount>
                                  <Amount><![CDATA[15.00]]></Amount>
                              </Discount>
                          </Coupon>
                      </CouponsAvailable>
                      <ProductReviews length="2">
                          <ProductReview id="1">
                              <Name><![CDATA[Jon Doe]]></Name>
                              <Review><![CDATA[This product is great!]]></Review>
                              <Date>
                                  <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                                  <Day><![CDATA[2]]></Day>
                                  <Month><![CDATA[10]]></Month>
                                  <Year><![CDATA[2009]]></Year>
                                  <Hour><![CDATA[12]]></Hour>
                                  <Minute><![CDATA[22]]></Minute>                       <Second><![CDATA[33]]></Second>
                              </Date>
                              <Approved>Boolean Types</Approved>
                          </ProductReview>
                          <ProductReview id="2">
                              <Name><![CDATA[Sally Johnson]]></Name>
                              <Review><![CDATA[I like this product!]]></Review>
                              <Date>
                                  <UnixTimeStamp><![CDATA[1111111]]></UnixTimeStamp>
                                  <Day><![CDATA[2]]></Day>
                                  <Month><![CDATA[10]]></Month>
                                  <Year><![CDATA[2009]]></Year>
                                  <Hour><![CDATA[12]]></Hour>
                                  <Minute><![CDATA[22]]></Minute>
                                  <Second><![CDATA[33]]></Second>
                              </Date>
                              <Approved>Boolean Types</Approved>
                          </ProductReview>
                      </ProductReviews>
                      <UseRegularTeaserAndDescriptionForMobile>Boolean
            Types</UseRegularTeaserAndDescriptionForMobile>
                      <MobileMainPhoto>
                          <Flag>Photo Flags</Flag>
                          <LocalFile>
                              <Name><![CDATA[mytest.jpg]]></Name>
                              <Extension><![CDATA[jpg]]></Extension>
                              <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                          </LocalFile>
                          <URL><![CDATA[http://www.mysite.com/myimage.jpg]]></URL>
                          <Width><![CDATA[100]]></Width>
                          <Height><![CDATA[200]]></Height>
                          <Languages length="2">
                              <LanguageData charset="ISO-8859-1" id="1">
                                  <Caption><![CDATA[Caption 1]]></Caption>
                                  <AltTitleTag><![CDATA[Alt/Title Tag 1]]></AltTitleTag>
                              </LanguageData>
                              <LanguageData charset="UTF-8" id="2">
                                  <Caption><![CDATA[Caption 1 (greek)]]></Caption>
                                  <AltTitleTag><![CDATA[Alt/Title Tag 1 (greek)]]></AltTitleTag>
                              </LanguageData>
                          </Languages>
                      </MobileMainPhoto>
                      <MobileLargePhoto>
                          <Flag>Photo Flags</Flag>
                          <LocalFile>
                              <Name><![CDATA[mytest.jpg]]></Name>
                              <Extension><![CDATA[jpg]]></Extension>
                              <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                          </LocalFile>
                          <URL><![CDATA[http://www.mysite.com/myimage.jpg]]></URL>
                          <Width><![CDATA[100]]></Width>
                          <Height><![CDATA[200]]></Height>
                      </MobileLargePhoto>
                      <AllowLowerPriceRequest>Boolean Types</AllowLowerPriceRequest>

            <CanonicalUrl><![CDATA[http://www.mysite.com/Apple-iPhone-3G.html]]></CanonicalUrl>
                      <SearchPriority><![CDATA[10]]></SearchPriority>
                      <ShowMsrpAndHideRetailPrice>Boolean Types</ShowMsrpAndHideRetailPrice>
                      <RequiresCustomOrderCompletePage>Boolean
            Types</RequiresCustomOrderCompletePage>
                      <CustomOrderCompleteId><![CDATA[456]]></CustomOrderCompleteId>
                      <DisplayAddThisButton>Boolean Types</DisplayAddThisButton>
                      <Attachments length="2">
                          <Attachment id="1">
                              <LocalFile>
                                  <Name><![CDATA[spec.pdf]]></Name>
                                  <Extension>pdf</Extension>
                                  <Data>lksjfsa;lfjsals;fjskafjsa;fjasdkfasjdfadfa</Data>
                              </LocalFile>
                          </Attachment>
                          <Attachment id="2">
                              <Url><![CDATA[http://www.mysite.com/pdf/diagram.pdf]]></Url>
                          </Attachment>
                      </Attachments>
                      <TemplateLayout><![CDATA[Pre-Designed 3]]></TemplateLayout>
                      <InventoryBundleProducts length="1">
                          <InventoryBundleProduct id="1">
                              <LanguageData charset="ISO-8859-1" name="English" id="1">
                                  <Name><![CDATA[Inventory Bundle Product]]></Name>
                              </LanguageData>
                              <Quantity><![CDATA[5]]></Quantity>
                          </InventoryBundleProduct>
                      </InventoryBundleProducts>
                      <FilterAttributes length="1">
                          <FilterAttribute id="1">
                              <LanguageData charset="ISO-8859-1" name="English" id="1">                       <Name><![CDATA[Color]]></Name>
                              </LanguageData>
                              <Options length="1">
                                  <Option id="1">
                                      <LanguageData charset="ISO-8859-1" name="English" id="1">
                                          <Name><![CDATA[Blue]]></Name>
                                      </LanguageData>
                                  </Option>
                              </Options>
                          </FilterAttribute>
                      </FilterAttributes>
                      <RestrictedShippingStates length="2">
                          <State><![CDATA[Tennessee]]></State>
                          <State><![CDATA[Ohio]]></State>
                      </RestrictedShippingStates>
                      <InternationalMailType>International Mail Type</InternationalMailType>
                      <InternationalMailType2>International Mail Type</InternationalMailType2>
                      <InternationalMailType3>International Mail Type</InternationalMailType3>
                      <InternationalMailType4>International Mail Type</InternationalMailType4>
                      <InternationalMailType5>International Mail Type</InternationalMailType5>
                      <NumberOfItemsPerBox><![CDATA[5]]></NumberOfItemsPerBox>           <GoogleProductsDescription><![CDATA[This product's "Google Products" description]]></GoogleProductsDescription>
                      <PasswordProtected>Boolean Types</PasswordProtected>
                      <Password><![CDATA[SuperSecretPass]]></Password>
                      <CustomFee>
                          <Languages length="1">
                              <LanguageData charset="ISO-8859-1" name="English" id="1">
                                  <Name><![CDATA[Custom Fee]]></Name>
                              </LanguageData>
                          </Languages>
                          <Fee>
                              <Amount>5.00</Amount>
                          </Fee>
                          <Type>Custom Fee Types</Type>
                      </CustomFee>
                      <SearchTerms><![CDATA[Test1,Test2]]></SearchTerms>
                      <MPN><![CDATA[GO1234568OOGLE]]></MPN>
                      <Brand><![CDATA[Acme]]></Brand>
                      <GoogleProductsCategory><![CDATA[Apparel &
            Accessories]]></GoogleProductsCategory>
                      <GoogleAvailability>Google Availability Type</GoogleAvailability>
                      <GoogleGender>Google Gender Type</GoogleGender>           <GoogleAgeGroup>Google Age Group Type</GoogleAgeGroup>
                      <IncludeInBingProductFeed>Boolean Types</IncludeInBingProductFeed>
                      <IncludeInGoogleProductFeed>Boolean Types</IncludeInGoogleProductFeed>
                      <SlugStyle><![CDATA[customauto]]></SlugStyle>
                      <UsePinterest>Boolean Types</UsePinterest>
                      <EchoFreightClass>Echo Freight Classes</EchoFreightClass>
                      <EchoFreightPalletQuantity><![CDATA[1]]></EchoFreightPalletQuantity>
                      <SoldInMultiplesOf><![CDATA[4]]></SoldInMultiplesOf>
                      <treatVariantsAsMainLevelInvItemsInQb>Boolean
            Types</treatVariantsAsMainLevelInvItemsInQb>
                      <includeProductInAdditionToVariantsInQbOrderXml>Boolean
            Types</includeProductInAdditionToVariantsInQbOrderXml>
                  </Product>
              </List>
            </Request>
        """
