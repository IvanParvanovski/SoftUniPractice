#pragma checksum "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "81ca3a517d7aab71be7a0ab9576ce8dc95f65f23"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Events_All), @"mvc.1.0.view", @"/Views/Events/All.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/_ViewImports.cshtml"
using Eventures.WebApp;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/_ViewImports.cshtml"
using Eventures.WebApp.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"81ca3a517d7aab71be7a0ab9576ce8dc95f65f23", @"/Views/Events/All.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"58b58c07b1ca6d5b5f8a564fbf56298daac4a360", @"/Views/_ViewImports.cshtml")]
    #nullable restore
    public class Views_Events_All : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<IEnumerable<EventViewModel>>
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
#line 3 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
  
    ViewData["Title"] = "All Events";

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n<h1>");
#nullable restore
#line 7 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
Write(ViewData["Title"]);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h1>\r\n\r\n<p>\r\n    ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("a", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "81ca3a517d7aab71be7a0ab9576ce8dc95f65f234125", async() => {
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
            WriteLiteral("\r\n</p>\r\n<table class=\"table\">\r\n    <thead>\r\n        <tr>\r\n            <th>\r\n                ");
#nullable restore
#line 16 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.Name));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                ");
#nullable restore
#line 19 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.Place));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                ");
#nullable restore
#line 22 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.Start));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                ");
#nullable restore
#line 25 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.End));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                ");
#nullable restore
#line 28 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.TotalTickets));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                ");
#nullable restore
#line 31 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.PricePerTicket));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                ");
#nullable restore
#line 34 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayNameFor(model => model.Owner));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </th>\r\n            <th>\r\n                Actions\r\n            </th>\r\n        </tr>\r\n    </thead>\r\n    <tbody>\r\n");
#nullable restore
#line 42 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
     foreach (var item in Model) {

#line default
#line hidden
#nullable disable
            WriteLiteral("        <tr>\r\n            <td>\r\n                ");
#nullable restore
#line 45 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.Name));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n                ");
#nullable restore
#line 48 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.Place));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n                ");
#nullable restore
#line 51 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.Start));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n                ");
#nullable restore
#line 54 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.End));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n                ");
#nullable restore
#line 57 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.TotalTickets));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n                ");
#nullable restore
#line 60 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.PricePerTicket));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n                ");
#nullable restore
#line 63 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
           Write(Html.DisplayFor(modelItem => item.Owner));

#line default
#line hidden
#nullable disable
            WriteLiteral("\r\n            </td>\r\n            <td>\r\n");
#nullable restore
#line 66 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
                 if (this.User.Identity.Name == item.Owner)
                {
                    

#line default
#line hidden
#nullable disable
#nullable restore
#line 68 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
               Write(Html.ActionLink("Delete", "Delete", new { id = item.Id }));

#line default
#line hidden
#nullable disable
            WriteLiteral("                    <span>|</span>\r\n");
#nullable restore
#line 70 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
               Write(Html.ActionLink("Edit", "Edit", new { id = item.Id }));

#line default
#line hidden
#nullable disable
#nullable restore
#line 70 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
                                                                          
                }

#line default
#line hidden
#nullable disable
            WriteLiteral("            </td>\r\n        </tr>\r\n");
#nullable restore
#line 74 "/Users/ivan_parvanovski/Desktop/SoftUniPractice/C#/Svetlina/legacy-code/legacy-code-skeleton/Eventures.WebApp/Views/Events/All.cshtml"
    }

#line default
#line hidden
#nullable disable
            WriteLiteral("    </tbody>\r\n</table>\r\n");
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
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<IEnumerable<EventViewModel>> Html { get; private set; } = default!;
        #nullable disable
    }
}
#pragma warning restore 1591