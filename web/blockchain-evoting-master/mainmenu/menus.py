MENUS = {

    # RETAIL MENU BELOW 
    'NAV_MENU_VOTER': [

        # underwriting section
          {
            "name": "BLOCK",
            "url": "reinsurance:index",
            "icon_class": 'mdi mdi-file-cabinet',
            "submenu": [
            # {
            #     "name": "View Reinsurance",
            #     "url": "reinsurance:index",
             
            # },

            {
                "name": "Create Ballot",
                "url": "ballot:create",
             
            },

           
        
            
        ],
        },

 
        # accounting section 

   

          # Administration section
        

    ] , 


     'NAV_MENU_ADMIN': [

      
 
        # accounting section 

   

          # Administration section
        {
            "name": "CHAIN",
            "url": "#",
            "icon_class": 'mdi mdi-file-cabinet',
            "submenu": [
                {
                    "name": "Verification",
                    "url": "simulation:generate",
                
                },
            
                {
                    "name": "See Transanctions",
                    "url": "simulation:transactions",
                
                },

                    {
                    "name": "Blocks",
                    "url": "simulation:blockchain",
                
                },

                 {
                "name": "Add Candidate ",
                "url": "ballot:create_candidate",
             
                    },  

                 {
                "name": "Delete All Candidates ",
                "url": "ballot:delete_candidate",
         
                },  
            
          
            
            ],
        },

    ]


    
}

