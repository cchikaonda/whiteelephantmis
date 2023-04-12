
// Data Tables Functionality Scripts
    $(function () {
        $("#search_item_table").DataTable({
            "responsive": true,
            "autoWidth": false,
        });

        $("#refunds_report_table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#refunds_report_table_wrapper .col-md-6:eq(0)');

        $("#stock-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#stock-table_wrapper .col-md-6:eq(0)');

        $("#stock-details").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#stock-details_wrapper .col-md-6:eq(0)');

        $("#unpaid_order_pos_dash_table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["csv", "pdf",]
        }).buttons().container().appendTo('#unpaid_order_pos_dash_table_wrapper .col-md-6:eq(0)');


        

        $("#batch-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#batch-table_wrapper .col-md-6:eq(0)');

        $("#supplier-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#supplier-table_wrapper .col-md-6:eq(0)');

        $("#user-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
        }).buttons().container().appendTo('#user-table_wrapper .col-md-6:eq(0)');

        $("#quotation_items_table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#quotation_items_table_wrapper .col-md-6:eq(0)');

        $("#quotation-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#quotation-table_wrapper .col-md-6:eq(0)');

        $("#out_of_stock_items_table").DataTable({
            "orderCellsTop": true,
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "pageLength":5,
            "buttons": ["copy", "csv", "excel", "pdf",]
        }).buttons().container().appendTo('#out_of_stock_items_table_wrapper .col-md-6:eq(0)');
        

        $("#sales_report_table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "pageLength":50,
            "order":[],
            "buttons": ["copy", "csv", "excel", "pdf", "print",]
        }).buttons().container().appendTo('#sales_report_table_wrapper .col-md-6:eq(0)');

        $("#expenses-category-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#expenses-category-table_wrapper .col-md-6:eq(0)');
      
        $("#expenses-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#expenses-table_wrapper .col-md-6:eq(0)');

        

        $("#orders-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#orders-table_wrapper .col-md-6:eq(0)');

        $('#unit-table').DataTable({
            "responsive":true,
            "lengthChange": false,
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#unit-table_wrapper .col-md-6:eq(0)');

        $('#item-table').DataTable({
            "responsive":true,
            "lengthChange": false,
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf",
            {
                              extend: 'print',
                              messageTop: 'Inventory Items',
                              exportOptions: {
                                  columns: ':visible',
                                  
                              }
                          },
                          'colvis'
                        ],
                          columnDefs: [ {
                              targets: -1,
                              visible: true
                          }
          ]
        }).buttons().container().appendTo('#item-table_wrapper .col-md-6:eq(0)');

        $("#customer-table").DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#customer-table_wrapper .col-md-6:eq(0)');

        $('#category-table').DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#category-table_wrapper .col-md-6:eq(0)');

        $('#fastsellingproduct-table').DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["excel", "pdf", "print"],
            // "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
        }).buttons().container().appendTo('#fastsellingproduct-table_wrapper .col-md-6:eq(0)');

        $('#customer-table-pos').DataTable({
            "responsive": true, 
            "lengthChange": false, 
            "autoWidth": false,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#customer-table-pos_wrapper .col-md-6:eq(0)');

        $('#inventory_quantity_table').DataTable({
            "responsive": true, 
            "lengthChange": true, 
            "autoWidth": false,
            "pageLength":50,
            "order":[],
            "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
            "buttons": ["copy", "csv", "excel", "pdf", "print",
            
          ]
        }).buttons().container().appendTo('#inventory_quantity_table_wrapper .col-md-6:eq(0)');

  
        $("#unsettled_orders_table").DataTable({
            "responsive": true,
            "autoWidth": false,
        });

        $('#unpaid-orders-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#quotation-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#example2').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": false,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#product-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#all-requisitions-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#pending-requisitions-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#denied-requisitions-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

        $('#approved-requisitions-table').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
        });

    });

// End Data Tables Functionality Scripts 