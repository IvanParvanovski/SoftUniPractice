#pragma checksum "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "468b182e3f82c6dfab71da55bd66420b304d960c4fbf20fcdf4e9dd1ba017cbe"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Events_All), @"mvc.1.0.view", @"/Views/Events/All.cshtml")]
namespace AspNetCore
{
    #line hidden
    using global::System;
    using global::System.Collections.Generic;
    using global::System.Linq;
    using global::System.Threading.Tasks;
    using global::Microsoft.AspNetCore.Mvc;
    using global::Microsoft.AspNetCore.Mvc.Rendering;
    using global::Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\_ViewImports.cshtml"
using Eventures.WebApp;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\_ViewImports.cshtml"
using Eventures.WebApp.Models;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\_ViewImports.cshtml"
using Eventures.Services.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA256", @"468b182e3f82c6dfab71da55bd66420b304d960c4fbf20fcdf4e9dd1ba017cbe", @"/Views/Events/All.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA256", @"c65c78a0290610f778c788a1e2713783bb0312ed9c323b60130ea8a71e09e22f", @"/Views/_ViewImports.cshtml")]
    #nullable restore
    public class Views_Events_All : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<IEnumerable<EventServiceModel>>
    #nullable disable
    {
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_0 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("asp-action", "Create", global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        #line hidden
        #pragma warning disable 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext __tagHelperExecutionContext;
        #pragma warning restore 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner __tagHelperRunner = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner();
        #pragma warning disable 0169
        private string __tagHelperStringValueBuffer;
        #pragma warning restore 0169
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __backed__tagHelperScopeManager = null;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __tagHelperScopeManager
        {
            get
            {
                if (__backed__tagHelperScopeManager == null)
                {
                    __backed__tagHelperScopeManager = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager(StartTagHelperWritingScope, EndTagHelperWritingScope);
                }
                return __backed__tagHelperScopeManager;
            }
        }
        private global::Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("\r\n");
#nullable restore
#line 3 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
  
	ViewData["Title"] = "All Events";

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n<h1>");
#nullable restore
#line 7 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
Write(ViewData["Title"]);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h1>\r\n\r\n<p>\r\n\t");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("a", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "468b182e3f82c6dfab71da55bd66420b304d960c4fbf20fcdf4e9dd1ba017cbe4586", async() => {
                WriteLiteral("Create New");
            }
            );
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper);
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.Action = (string)__tagHelperAttribute_0.Value;
            __tagHelperExecutionContext.AddTagHelperAttribute(__tagHelperAttribute_0);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\r\n</p>\r\n<table class=\"table\">\r\n\t<thead>\r\n\t\t<tr>\r\n\t\t\t<th>\r\n\t\t\t\t");
#nullable restore
#line 16 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
           Write(Html.DisplayNameFor(model => model.Name));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t</th>\r\n\t\t\t<th>\r\n\t\t\t\t");
#nullable restore
#line 19 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
           Write(Html.DisplayNameFor(model => model.Place));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t</th>\r\n\t\t\t<th>\r\n\t\t\t\t");
#nullable restore
#line 22 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
           Write(Html.DisplayNameFor(model => model.Start));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t</th>\r\n\t\t\t<th>\r\n\t\t\t\t");
#nullable restore
#line 25 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
           Write(Html.DisplayNameFor(model => model.End));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t</th>\r\n\t\t\t<th>\r\n\t\t\t\tActions\r\n\t\t\t</th>\r\n\t\t</tr>\r\n\t</thead>\r\n\t<tbody>\r\n");
#nullable restore
#line 33 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
         foreach (var item in Model)
		{

#line default
#line hidden
#nullable disable
            WriteLiteral("\t\t\t<tr>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t");
#nullable restore
#line 37 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
               Write(Html.DisplayFor(modelItem => item.Name));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t\t</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t");
#nullable restore
#line 40 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
               Write(Html.DisplayFor(modelItem => item.Place));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t\t</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t");
#nullable restore
#line 43 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
               Write(Html.DisplayFor(modelItem => item.Start));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t\t</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t");
#nullable restore
#line 46 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
               Write(Html.DisplayFor(modelItem => item.End));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n\t\t\t\t</td>\r\n\t\t\t\t<td>\r\n");
#nullable restore
#line 49 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                     if (this.User.Identity.Name == item.Owner)
					{
						

#line default
#line hidden
#nullable disable
#nullable restore
#line 51 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                   Write(Html.ActionLink("Delete", "Delete", new { id = item.Id }));

#line default
#line hidden
#nullable disable
            WriteLiteral("\t\t\t\t\t\t<span>|</span>\r\n");
#nullable restore
#line 53 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                   Write(Html.ActionLink("Edit", "Edit", new { id = item.Id }));

#line default
#line hidden
#nullable disable
            WriteLiteral("\t\t\t\t\t\t<span>|</span>\r\n\t\t\t\t\t\t<a href=\"#\"");
            BeginWriteAttribute("id", " id=\"", 1112, "\"", 1133, 2);
            WriteAttributeValue("", 1117, "details-", 1117, 8, true);
#nullable restore
#line 55 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1125, item.Id, 1125, 8, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            BeginWriteAttribute("onclick", " onclick=\"", 1134, "\"", 1243, 15);
            WriteAttributeValue("", 1144, "details(", 1144, 8, true);
#nullable restore
#line 55 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1152, item.Id, 1152, 8, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1160, ",", 1160, 1, true);
            WriteAttributeValue(" ", 1161, "\'", 1162, 2, true);
#nullable restore
#line 55 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1163, item.TotalTickets, 1163, 18, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1181, "\',", 1181, 2, true);
            WriteAttributeValue(" ", 1183, "\'", 1184, 2, true);
#nullable restore
#line 55 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1185, item.PricePerTicket, 1185, 20, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1205, "\',", 1205, 2, true);
            WriteAttributeValue(" ", 1207, "\'", 1208, 2, true);
#nullable restore
#line 55 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1209, item.Description, 1209, 17, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1226, "\',", 1226, 2, true);
            WriteAttributeValue(" ", 1228, "\'", 1229, 2, true);
#nullable restore
#line 55 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1230, item.Owner, 1230, 11, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1241, "\')", 1241, 2, true);
            EndWriteAttribute();
            WriteLiteral(">View Details</a>\r\n");
#nullable restore
#line 56 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
					}
					else
					{

#line default
#line hidden
#nullable disable
            WriteLiteral("\t\t\t\t\t\t<a href=\"#\"");
            BeginWriteAttribute("id", " id=\"", 1307, "\"", 1328, 2);
            WriteAttributeValue("", 1312, "details-", 1312, 8, true);
#nullable restore
#line 59 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1320, item.Id, 1320, 8, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            BeginWriteAttribute("onclick", " onclick=\"", 1329, "\"", 1438, 15);
            WriteAttributeValue("", 1339, "details(", 1339, 8, true);
#nullable restore
#line 59 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1347, item.Id, 1347, 8, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1355, ",", 1355, 1, true);
            WriteAttributeValue(" ", 1356, "\'", 1357, 2, true);
#nullable restore
#line 59 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1358, item.TotalTickets, 1358, 18, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1376, "\',", 1376, 2, true);
            WriteAttributeValue(" ", 1378, "\'", 1379, 2, true);
#nullable restore
#line 59 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1380, item.PricePerTicket, 1380, 20, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1400, "\',", 1400, 2, true);
            WriteAttributeValue(" ", 1402, "\'", 1403, 2, true);
#nullable restore
#line 59 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1404, item.Description, 1404, 17, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1421, "\',", 1421, 2, true);
            WriteAttributeValue(" ", 1423, "\'", 1424, 2, true);
#nullable restore
#line 59 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1425, item.Owner, 1425, 11, false);

#line default
#line hidden
#nullable disable
            WriteAttributeValue("", 1436, "\')", 1436, 2, true);
            EndWriteAttribute();
            WriteLiteral(">View Details</a>\r\n");
#nullable restore
#line 60 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
					}

#line default
#line hidden
#nullable disable
            WriteLiteral("\t\t\t\t</td>\r\n\t\t\t</tr>\r\n\t\t\t<tr");
            BeginWriteAttribute("class", " class=\"", 1493, "\"", 1509, 1);
#nullable restore
#line 63 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
WriteAttributeValue("", 1501, item.Id, 1501, 8, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            WriteLiteral(" style=\"display: none;\">\r\n\t\t\t\t<td colspan=\"5\">\r\n\t\t\t\t\t<table>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<th>");
#nullable restore
#line 67 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayNameFor(modelItem => item.TotalTickets));

#line default
#line hidden
#nullable disable
            WriteLiteral("</th>\r\n\t\t\t\t\t\t\t<td>");
#nullable restore
#line 68 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayFor(modelItem => item.TotalTickets));

#line default
#line hidden
#nullable disable
            WriteLiteral("</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<th>");
#nullable restore
#line 71 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayNameFor(modelItem => item.PricePerTicket));

#line default
#line hidden
#nullable disable
            WriteLiteral("</th>\r\n\t\t\t\t\t\t\t<td>");
#nullable restore
#line 72 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayFor(modelItem => item.PricePerTicket));

#line default
#line hidden
#nullable disable
            WriteLiteral("</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<th>");
#nullable restore
#line 75 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayNameFor(modelItem => item.Description));

#line default
#line hidden
#nullable disable
            WriteLiteral("</th>\r\n\t\t\t\t\t\t\t<td>");
#nullable restore
#line 76 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.Raw(item.Description));

#line default
#line hidden
#nullable disable
            WriteLiteral("</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<th>");
#nullable restore
#line 79 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayNameFor(modelItem => item.Owner));

#line default
#line hidden
#nullable disable
            WriteLiteral("</th>\r\n\t\t\t\t\t\t\t<td>");
#nullable restore
#line 80 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
                           Write(Html.DisplayFor(modelItem => item.Owner));

#line default
#line hidden
#nullable disable
            WriteLiteral("</td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</table>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n");
#nullable restore
#line 85 "C:\Users\marsr\Desktop\SoftUniSvetlina\12grade\04.Working-with-Legacy-Code-Exercise-Solutions\Eventures.WebApp\Views\Events\All.cshtml"
		}

#line default
#line hidden
#nullable disable
            WriteLiteral(@"	</tbody>
</table>

<script>
	function details(id, total, price, desc, owner) {
		var table = $(`.${id}`);
		var button = $(`#details-${id}`);

		if (table.css(""display"") == ""none"") {
			table.css(""display"", ""table-row"");
			button.text(""Hide Details"");
		} else if (table.css(""display"") == ""table-row"") {
			table.css(""display"", ""none"");
			button.text(""View Details"");
		}
	}
</script>
");
        }
        #pragma warning restore 1998
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; } = default!;
        #nullable disable
        #nullable restore
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<IEnumerable<EventServiceModel>> Html { get; private set; } = default!;
        #nullable disable
    }
}
#pragma warning restore 1591
