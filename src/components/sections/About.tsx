import { motion } from "framer-motion"
import { PROFILE } from "@/data/profile"
import { Card, CardContent } from "@/components/ui/card"

export const About = () => {
    return (
        <section id="about" className="py-20 scroll-mt-16">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5 }}
                className="space-y-8"
            >
                <h2 className="text-3xl font-bold tracking-tight">About Me</h2>
                <div className="grid md:grid-cols-2 gap-8 items-center">
                    <div className="space-y-4">
                        <p className="text-lg text-muted-foreground leading-relaxed">
                            {PROFILE.about}
                        </p>
                        <p className="text-lg text-muted-foreground leading-relaxed">
                            My engineering philosophy revolves around stability, resilience, and automation.
                            If a task needs to be done more than twice, I automate it.
                        </p>
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                        <Card className="bg-muted/50 border-none">
                            <CardContent className="flex flex-col items-center justify-center p-6 text-center space-y-2">
                                <span className="text-4xl font-bold text-primary">5+</span>
                                <span className="text-sm text-muted-foreground">Years Experience</span>
                            </CardContent>
                        </Card>
                        <Card className="bg-muted/50 border-none">
                            <CardContent className="flex flex-col items-center justify-center p-6 text-center space-y-2">
                                <span className="text-4xl font-bold text-primary">20+</span>
                                <span className="text-sm text-muted-foreground">Projects Delivered</span>
                            </CardContent>
                        </Card>
                        <Card className="bg-muted/50 border-none">
                            <CardContent className="flex flex-col items-center justify-center p-6 text-center space-y-2">
                                <span className="text-4xl font-bold text-primary">100%</span>
                                <span className="text-sm text-muted-foreground">Data Integrity</span>
                            </CardContent>
                        </Card>
                        <Card className="bg-muted/50 border-none">
                            <CardContent className="flex flex-col items-center justify-center p-6 text-center space-y-2">
                                <span className="text-4xl font-bold text-primary">∞</span>
                                <span className="text-sm text-muted-foreground">Automation Passion</span>
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </motion.div>
        </section>
    )
}
