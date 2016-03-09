define('app/templates/libs/all', [], function() {
  'use strict';

  return  '<div class="content-page-libs-all">' +
            '<h2 data-bind="text: $data.title"></h2>' +
            '<div style="background-color: #2196f3; border-color: #2196f3" class="alert alert-info">' +
              '<span>This project would not exist without the help of the following great libraries.</span>' +
            '</div>' +
            '<ul data-bind="foreach: $data.libraries" class="list-unstyled">' +
              '<li>' +
                '<div style="color: #2196f3" class="hand fade">' +
                  '<i class="fa fa-hand-o-right"></i>' +
                  '&nbsp;' +
                '</div>' +
                '<a data-bind="attr: {href: \'#/libs/view/\' + encodeURIComponent($data.name)}, text: $data.title"></a>' +
              '</li>' +
            '</ul>' +
            '<h2>Template</h2>' +
            '<div class="panel panel-primary">' +
              '<div class="panel-heading">Template provided by</div>' +
              '<div class="panel-body">' +
              '<p>' +
                '<a href="https://github.com/crissdev/spa-template-ko/" title="GitHub Project" style="padding-right: 10.5px;">' +
                  '<i class="fa fa fa-github"></i>' +
                '</a>' +
                '&copy;&nbsp;' +
                '<a href="http://crissdev.com">Cristian Trifan</a>' +
              '</p>' +
              '<p>' +
                '<span>Lisence type: MIT</span>' +
              '</p>' +
            '</div>' +
          '</div>';
});