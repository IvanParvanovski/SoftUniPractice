using System;
using Microsoft.Build.Framework;

namespace FinalProject.Models
{
    public class Message
    {
        public int Id { get; set; }
        [Required]
        
        public string UserName { get; set; }
        [Required]
        
        public string Text { get; set; }
        
        public DateTime When { get; set; }
        
        public string UserID { get; set; }
        
        public virtual AppUser AppUser { get; set; }
    }
}