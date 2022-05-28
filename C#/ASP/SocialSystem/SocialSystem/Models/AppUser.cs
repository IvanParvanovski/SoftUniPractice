using System.Collections;
using System.Collections.Generic;
using Microsoft.AspNetCore.Identity;

namespace SocialSystem.Models
{
    public class AppUser : IdentityUser
    {
        // 1 - * AppUser || Message
        public virtual ICollection<Message> Messages { get; set; }

        public AppUser()
        {
            Messages = new HashSet<Message>();
        }
        
    }
}