var object = [
    {
      title: '北京盈科中心A座',
      start: '2017-03-01T14:00:00',
      end: '2017-03-01T15:00:00',
      url: '#',
      className: 'full-event',
    },
    {
      title: '北京盈科中心A座',
      start: '2017-03-02T14:00:00',
      end: '2017-03-02T15:00:00',
      url: '#',
      className: 'near-full-event',
    },
    {
      title: '北京盈科中心A座',
      start: '2017-03-03T14:00:00',
      end: '2017-03-03T15:00:00',
      url: '#'
    },
    {
      title: '北京盈科中心A座',
      start: '2017-03-07T14:00:00',
      end: '2017-03-07T15:00:00',
      url: '#'
    },
    {
      title: '北京盈科中心A座',
      start: '2017-03-09T14:00:00',
      end: '2017-03-09T15:00:00',
      url: '#'
    },
    {
      title: '北京盈科中心A座',
      start: '2017-03-12T14:00:00',
      end: '2017-03-12T15:00:00',
      url: '#'
    },
]

$('#calendar').fullCalendar({
  header: {
		left: 'prev,next today',
		center: 'title',
		right: 'month,agendaWeek,agendaDay'
	},
  editable: false,
  events: object
});
