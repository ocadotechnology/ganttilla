import {Component, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ChartReadyEvent, ChartSelectEvent} from 'ng2-google-charts';
import {Goal, StaticFileService} from '../services/static-file.service';

@Component({
    selector: 'app-chart',
    templateUrl: './chart.component.html',
    styleUrls: ['./chart.component.css']
})
export class ChartComponent implements OnInit {
    milestones: Goal[];
    filteredId = [];
    swimlanes = new Set();
    @ViewChild('cchart') cchart;

    chartData = {
        chartType: 'Timeline',
        dataTable: [
            ['Label', 'Name', 'From', 'To'],
            ['Label', 'Dummy', new Date(2018, 0, 1), new Date(2018, 11, 31)]
        ],
        options: {
            height: 700,
            timeline: {
                groupByRowLabel: true,
                colorByRowLabel: true,
                rowLabelStyle: {fontName: 'Roboto'},
                barLabelStyle: {fontName: 'Roboto'}
            }
        }
    };


    constructor(private route: ActivatedRoute,
                private staticFileService: StaticFileService) {

        this.route.params.subscribe(params => {
            let teamName = params['teamName'];
            this.chartData.dataTable = [['Label', 'Name', 'From', 'To']];

            this.staticFileService.getFile(`${teamName}.json`).subscribe(goals => {
                this.milestones = goals;
                const DONT_DISPLAY_FLAG = '#NOT_ON_ROADMAP';
                var regex = RegExp(DONT_DISPLAY_FLAG);
                this.filteredId = [0];
                this.swimlanes = new Set();

                this.milestones
                    .filter(milestone => !regex.test(milestone.description))
                    .filter(milestone => milestone.start_date !== null)
                    .filter(milestone => milestone.end_date !== null)
                    .sort((a, b) => new Date(a.end_date).getTime() - new Date(b.end_date).getTime())
                    .map(milestone => {
                        if (!milestone.category) {
                            const cat = milestone.swimlane;
                            milestone.category = cat ? cat : milestone.title;
                        }
                        this.swimlanes.add(milestone.category);
                        this.chartData.dataTable.push(
                            [milestone.category, milestone.title, new Date(milestone.start_date), new Date(milestone.end_date)]);
                        this.filteredId.push(milestone.link);
                    });
                this.chartData = Object.create(this.chartData);
            });
        });

    }

    ngOnInit() {
        console.log('Chart component - onInit');
    } // ngOnInit - end


    public clicked(event: ChartSelectEvent) {
        let url = this.filteredId[event.row + 1];
        window.open(url, '_blank');
    }

    public ready(event: ChartReadyEvent) {
        let container = document.getElementById('timeline');
        let googleChartWrapper = this.cchart.wrapper;
        let dateRangeStart = googleChartWrapper.getDataTable().getColumnRange(2);
        let dateRangeEnd = googleChartWrapper.getDataTable().getColumnRange(3);
        // let options = {height: 41 * (this.chartData.dataTable.length - 1)};
        let options = {height: 41 * this.swimlanes.size - 1};


        function addMarker(markerDate) {
            let baseline;
            let baselineBounds;
            let chartElements;
            let markerLabel;
            let markerLine;
            let markerSpan;
            let svg;
            let timeline;
            let timelineUnit;
            let timelineWidth;
            let timespan;
            let height;

            baseline = null;
            timeline = null;
            svg = null;
            markerLabel = null;
            chartElements = container.getElementsByTagName('svg');
            if (chartElements.length > 0) {
                svg = chartElements[chartElements.length - 1];
                height = svg.getElementsByTagName('g')[0].getBBox().height;
            }
            chartElements = container.getElementsByTagName('rect');
            if (chartElements.length > 0) {
                timeline = chartElements[0];
            }
            chartElements = container.getElementsByTagName('path');
            if (chartElements.length > 0) {
                baseline = chartElements[0];
            }
            chartElements = container.getElementsByTagName('text');
            if (chartElements.length > 0) {
                markerLabel = chartElements[0].cloneNode(true);
            }
            if ((svg === null) || (timeline === null) || (baseline === null) || (markerLabel === null) ||
                (markerDate.getTime() < dateRangeStart.min.getTime()) ||
                (markerDate.getTime() > dateRangeEnd.max.getTime())) {
                return;
            }

            // calculate placement
            timelineWidth = parseFloat(timeline.getAttribute('width'));
            baselineBounds = baseline.getBBox();
            timespan = dateRangeEnd.max.getTime() - dateRangeStart.min.getTime();
            timelineUnit = (timelineWidth - baselineBounds.x) / timespan;
            markerSpan = markerDate.getTime() - dateRangeStart.min.getTime();

            // add line
            markerLine = timeline.cloneNode(true);
            markerLine.setAttribute('y', 0);
            markerLine.setAttribute('x', (baselineBounds.x + (timelineUnit * markerSpan)));
            markerLine.setAttribute('height', height);
            markerLine.setAttribute('width', 1);
            markerLine.setAttribute('stroke', 'none');
            markerLine.setAttribute('stroke-width', '0');
            markerLine.setAttribute('fill', '#e91e63');
            svg.appendChild(markerLine);
        }

        addMarker(new Date());
    }

    onResize(event) {
        this.chartData = Object.create(this.chartData);
    }

}
